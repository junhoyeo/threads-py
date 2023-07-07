import re
import json
import requests

from threadspy.types.threads_user import ThreadsUser
from threadspy.types import (
    GetUserProfileResponse,
    GetThreadLikersResponse,
    GetUserProfileThreadResponse,
    GetUserProfileRepliesResponse,
    GetUserProfileThreadsResponse,
)


class ThreadsAPI:
    fbLSDToken = "NjppQDEgONsU_1LCzrmp6q"  # FIXME: Remove default value
    verbose = False
    http_client = requests.Session()

    def __init__(self, options=None):
        if options and "fbLSDToken" in options:
            self.fbLSDToken = options["fbLSDToken"]
        if options and "verbose" in options:
            self.verbose = options.verbose

    def _get_default_headers(self, username):
        return {
            "authority": "www.threads.net",
            "accept": "*/*",
            "accept-language": "ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7",
            "cache-control": "no-cache",
            "origin": "https://www.threads.net",
            "pragma": "no-cache",
            "referer": f"https://www.threads.net/@{username}",
            "x-asbd-id": "129477",
            "x-fb-lsd": self.fbLSDToken,
            "x-ig-app-id": "238260118697367",
        }

    def get_user_id_from_username(self, username, options=None) -> str:
        headers = self._get_default_headers(username)
        response = self.http_client.get(f"https://www.threads.net/@{username}", headers=headers)
        headers["accept"] = (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        )
        headers["accept-language"] = "ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7"
        headers["pragma"] = "no-cache"
        headers["referer"] = "https://www.instagram.com/"
        headers["sec-fetch-dest"] = "document"
        headers["sec-fetch-mode"] = "navigate"
        headers["sec-fetch-site"] = "cross-site"
        headers["sec-fetch-user"] = "?1"
        headers["upgrade-insecure-requests"] = "1"
        headers["x-asbd-id"] = None
        headers["x-fb-lsd"] = None
        headers["x-ig-app-id"] = None
        text = response.text.replace("\n", "")

        user_id_match = re.search(r'"props":{"user_id":"(\d+)"},', text)
        user_id = user_id_match.group(1) if user_id_match else None

        lsd_token_match = re.search(r'"LSD",\[\],{"token":"(\w+)"},\d+\]', text)
        lsd_token = lsd_token_match.group(1) if lsd_token_match else None
        if options is not None and options.fbLSDToken is not None:
            self.fbLSDToken = lsd_token
            if self.verbose:
                print("[fbLSDToken] UPDATED", self.fbLSDToken)

        return user_id

    def get_user_profile(self, username, user_id=None):
        """
        Requires username and as an optional parameter user_id.
        If no user_id is passed then the function will automatically get user_id by
        resolving username.
        """
        if not user_id:
            user_id = self.get_user_id_from_username(username)
        headers = self._get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileRootQuery"

        params = {
            "lsd": self.fbLSDToken,
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "23996318473300828",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )
        user = GetUserProfileResponse.from_dict(response.json())
        return user.data.userData.user

    def get_user_profile_threads(self, username: str, user_id: str):
        """
        Returns user profile threads as a dict

        Args:
            username (string): username on threads.net
            user_id (string): user_id which is unique to each user.

        Returns:
            dict: list of user profile threads.
        """
        headers = self._get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileThreadsTabQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "6232751443445612",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )
        threads = GetUserProfileThreadsResponse.from_dict(response.json())
        return threads.data.mediaData.threads

    def get_user_profile_replies(self, username: str, user_id: str):
        """
        Returns user profile replies as a list

        Args:
            username (string): username on threads.net
            user_id (string): user_id which is unique to each user.

        Returns:
            dict: list of user profile threads.
        """
        headers = self._get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileRepliesTabQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "6307072669391286",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )
        replies = GetUserProfileRepliesResponse.from_dict(response.json())
        return replies.data.mediaData.threads

    def get_user_profile_thread(self, username: str, post_id: str):
        """
        Returns a thread info

        Args:
            username (string): username on threads.net
            post_id (string): post_id which is unique to each post.

        Returns:
            dict: a thread info.
        """
        headers = self._get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaPostPageQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"postID":"{post_id}"}}',
            "doc_id": "5587632691339264",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )
        thread = GetUserProfileThreadResponse.from_dict(response.json())
        return thread.data.data.containing_thread

    def get_thread_likers(self, username: str, post_id: str):
        """
        Returns a thread likers

        Args:
            username (string): username on threads.net
            post_id (string): post_id which is unique to each post.

        Returns:
            dict: a thread info.
        """
        headers = self._get_default_headers(username)

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"mediaID":"{post_id}"}}',
            "doc_id": "9360915773983802",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )
        thread = GetThreadLikersResponse.from_dict(response.json())
        return thread.data.likers
