import os
import re
import time
import json
import uuid
import base64
import urllib
from urllib.parse import quote
import random
import requests
import mimetypes
from typing import List
from datetime import datetime
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import (
    AES,
    PKCS1_v1_5,
)

from threadspy.types import (
    Thread,
    UsersData,
    ThreadsUser,
    ThreadData,
    GetUserProfileResponse,
    GetThreadLikersResponse,
    GetUserProfileThreadResponse,
    GetUserProfileRepliesResponse,
    GetUserProfileThreadsResponse,
)

from threadspy.constants import (
    LATEST_ANDROID_APP_VERSION,
    DEFAULT_LSD_TOKEN,
    DEFAULT_DEVICE_ID,
    BASE_API_URL,
)


class ThreadsAPI:
    fbLSDToken = DEFAULT_LSD_TOKEN
    verbose = False
    noUpdateLSD = False
    username = None
    password = None
    user_id = None
    token = None
    device_id = DEFAULT_DEVICE_ID
    http_client = requests.Session()
    timestamp_string = None
    encrypted_password = None

    def __init__(
        self,
        verbose: True | False = None,
        noUpdateLSD: str | None = None,
        fbLSDToken: str | None = None,
        username: str | None = None,
        password: str | None = None,
        device_id: str | None = None,
        token: str | None = None,
    ) -> None:
        if fbLSDToken is not None and isinstance(fbLSDToken, str):
            self.fbLSDToken = fbLSDToken
        if device_id is not None and isinstance(device_id, str):
            self.device_id = device_id
        if noUpdateLSD is not None and isinstance(noUpdateLSD, str):
            self.noUpdateLSD = noUpdateLSD
        if verbose is not None and isinstance(verbose, bool):
            self.verbose = verbose

        if (
            username is not None
            and isinstance(username, str)
            and password is not None
            and isinstance(password, str)
        ):
            self.username = username
            self.password = password
            self.public_key, self.public_key_id = self._get_ig_public_key()
            self.encrypted_password, self.timestamp_string = self._password_encryption(
                password
            )

        if token is not None and isinstance(token, str):
            self.token = token
        else:
            self.token = self.get_token()
            self.user_id = self.get_user_id_from_username(username)

    def __is_valid_url(self, url: str) -> bool:
        url_pattern = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
        if re.match(url_pattern, url) is not None:
            try:
                response = requests.head(url)
                return response.status_code == 200 or response.status_code == 302
            except requests.exceptions.RequestException as e:
                return False
        return False

    def __download(self, url: str) -> bytes:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print("[ERROR] fail to file load: ", e)
            return None

    def __get_app_headers(self) -> dict:
        headers = {
            "User-Agent": f"Barcelona {LATEST_ANDROID_APP_VERSION} Android",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        if self.token is not None:
            headers["Authorization"] = f"Bearer IGT:2:{self.token}"
        return headers

    def __get_default_headers(self, username: str = None) -> dict:
        headers = {
            "authority": "www.threads.net",
            "accept": "*/*",
            "accept-language": "ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7",
            "cache-control": "no-cache",
            "origin": "https://www.threads.net",
            "pragma": "no-cache",
            "x-asbd-id": "129477",
            "x-fb-lsd": self.fbLSDToken,
            "x-ig-app-id": "238260118697367",
        }

        if username is not None:
            self.username = username
            headers["referer"] = f"https://www.threads.net/@{username}"

        return headers

    def _get_ig_public_key(self) -> tuple[str, int]:
        """
        Get Instagram public key to encrypt the password.

        Returns:
            The public key and the key identifier as tuple(str, int).
        """
        str_parameters = json.dumps(
            {
                "id": str(uuid.uuid4()),
            },
        )
        encoded_parameters = quote(string=str_parameters, safe="!~*'()")

        response = requests.post(
            url=f"{BASE_API_URL}/api/v1/qe/sync/",
            headers={
                "User-Agent": f"Barcelona {LATEST_ANDROID_APP_VERSION} Android",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            },
            data=f"params={encoded_parameters}",
        )
        public_key = response.headers.get("ig-set-password-encryption-pub-key")
        public_key_id = response.headers.get("ig-set-password-encryption-key-id")

        return public_key, int(public_key_id)

    def _password_encryption(self, password: str) -> tuple[str, str]:
        password_bytes = password.encode("utf-8")

        timestamp = int(time.time())
        timestamp_string = str(timestamp).encode("utf-8")

        secret_key = get_random_bytes(32)
        key_id_mixed_bytes = int(1).to_bytes(1, "big") + self.public_key_id.to_bytes(
            1, "big"
        )
        initialization_vector = get_random_bytes(12)
        encrypted_rsa_key_mixed_bytes = int(0).to_bytes(1, "big") + int(1).to_bytes(
            1, "big"
        )
        public_key_bytes = base64.b64decode(self.public_key)
        public_key = RSA.import_key(extern_key=public_key_bytes)
        cipher = PKCS1_v1_5.new(public_key)
        encrypted_secret_key = cipher.encrypt(secret_key)
        cipher = AES.new(secret_key, AES.MODE_GCM, nonce=initialization_vector)
        cipher.update(timestamp_string)
        encrypted_password, auth_tag = cipher.encrypt_and_digest(password_bytes)

        password_as_encryption_sequence = (
            key_id_mixed_bytes
            + initialization_vector
            + encrypted_rsa_key_mixed_bytes
            + encrypted_secret_key
            + auth_tag
            + encrypted_password
        )
        password_encryption_base64 = base64.b64encode(
            s=password_as_encryption_sequence,
        ).decode("ascii")

        return password_encryption_base64, str(timestamp)

    def get_user_id_from_username(self, username) -> str:
        """
        set user id by username.

        Args:
            username (str): username on threads.net

        Returns:
            string: user_id if not valid return None
        """
        headers = self.__get_default_headers(username)
        headers.update(
            {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7",
                "pragma": "no-cache",
                "referer": "https://www.instagram.com/",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "x-asbd-id": None,
                "x-fb-lsd": None,
                "x-ig-app-id": None,
            }
        )
        response = self.http_client.get(
            f"https://www.instagram.com/{username}", headers=headers
        )

        text = response.text.replace("\n", "")

        user_id_match = re.search('"user_id":"(\d+)",', text)
        user_id = user_id_match.group(1) if user_id_match else None

        lsd_token_match = re.search('"LSD",\[\],{"token":"(\w+)"},\d+\]', text)
        lsd_token = lsd_token_match.group(1) if lsd_token_match else None

        if not self.noUpdateLSD and self.fbLSDToken is not None:
            self.fbLSDToken = lsd_token
            if self.verbose:
                print("[fbLSDToken] UPDATED", self.fbLSDToken)
        if user_id is not None:
            self.user_id = user_id
            return self.user_id
        else:
            return None

    def get_current_user_id(self) -> str:
        if self.user_id:
            if self.verbose:
                print("[userID] USING", self.user_id)
            return self.user_id
        if self.username is None:
            raise "username is not defined"
        self.user_id = self.get_user_id_from_username(self.username)
        if self.verbose:
            print("[userID] UPDATED", self.user_id)
        return self.user_id

    def get_user_profile(self, username, user_id=None) -> ThreadsUser:
        """
        Returns profile info by username.

        Args:
            username (str): username on threads.net
            user_id (str, optional):: user_id which is unique to each user.

        Returns:
            ThreadsUser: a profile info.
        """
        if self.verbose:
            print("[fbLSDToken] USING", self.fbLSDToken)

        if not user_id:
            user_id = self.get_user_id_from_username(username)
        headers = self.__get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileRootQuery"

        params = {
            "lsd": self.fbLSDToken,
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "23996318473300828",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )

        try:
            user = GetUserProfileResponse.from_dict(response.json())
            return user.data.userData.user
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return ThreadsUser(
                pk="",
                full_name="",
                profile_pic_url="",
                follower_count=0,
                is_verified=False,
                username="",
                profile_context_facepile_users=None,
                id=None,
            )

    def get_user_profile_threads(self, username: str, user_id: str) -> List[Thread]:
        """
        Returns a list of threads posted in the profile.

        Args:
            username (str): username on threads.net
            user_id (str): user_id which is unique to each user.

        Returns:
            List[Thread]: list of threads posted in the profile.
        """
        if self.verbose:
            print("[fbLSDToken] USING", self.fbLSDToken)
        headers = self.__get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileThreadsTabQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "6232751443445612",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )

        try:
            threads = GetUserProfileThreadsResponse.from_dict(response.json())
            return threads.data.mediaData.threads
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return []

    def get_user_profile_replies(self, username: str, user_id: str) -> List[Thread]:
        """
        Returns a list of replies in the thread.

        Args:
            username (str): username on threads.net
            user_id (str): user_id which is unique to each user.

        Returns:
            List[Thread]: list of replies in the thread.
        """
        if self.verbose:
            print("[fbLSDToken] USING", self.fbLSDToken)
        headers = self.__get_default_headers(username)
        headers["x-fb-friendly-name"] = "BarcelonaProfileRepliesTabQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"userID":"{user_id}"}}',
            "doc_id": "6684830921547925",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )

        try:
            replies = GetUserProfileRepliesResponse.from_dict(response.json())
            return replies.data.mediaData.threads
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return []

    def get_post_id_from_thread_id(self, thread_id: str) -> str:
        """
        Returns a thread info from thread id.

        Args:
            thread_id (str): thread_id which is unique to each thread.

        Returns:
            str: a post id
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
        post_id = 0
        for letter in thread_id:
            post_id = (post_id * 64) + alphabet.index(letter)

        return str(post_id)

    def get_post_id_from_url(self, post_url) -> str:
        """
        Returns the post_id of a specific one thread.

        Args:
            post_url (str): a threads app direct link

        Returns:
            str: a post id
        """
        response = requests.get(post_url)
        text = response.text
        text = text.replace("\n", "")
        post_id_match = re.search(r'{"post_id":"(.*?)"', text)
        post_id = post_id_match.group(1) if post_id_match else None

        lsd_token_match = re.search(r'"LSD",\[\],{"token":"(\w+)"},\d+\]', text)
        lsd_token = lsd_token_match.group(1) if lsd_token_match else None

        if not self.noUpdateLSD and self.fbLSDToken is not None:
            self.fbLSDToken = lsd_token
            if self.verbose:
                print("[fbLSDToken] UPDATED", self.fbLSDToken)
        return post_id

    def get_threads(self, post_id: str) -> ThreadData:
        """
        Returns a thread info from post id.

        Args:
            post_id (str): post_id which is unique to each post.

        Returns:
            ThreadData: a thread info
        """
        if self.verbose:
            print("[fbLSDToken] USING", self.fbLSDToken)
        headers = self.__get_default_headers()
        headers["x-fb-friendly-name"] = "BarcelonaPostPageQuery"

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"postID":"{post_id}"}}',
            "doc_id": "5587632691339264",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )

        try:
            thread = GetUserProfileThreadResponse.from_dict(response.json())
            return thread.data.data
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return ThreadData(containing_thread=None, reply_threads=[])

    def get_thread_likers(self, post_id: str) -> UsersData:
        """
        Returns a thread likers

        Args:
            post_id (str): post_id which is unique to each post.

        Returns:
            UsersData: a thread likers
        """
        if self.verbose:
            print("[fbLSDToken] USING", self.fbLSDToken)
        headers = self.__get_default_headers()

        params = {
            "lsd": f"{self.fbLSDToken}",
            "variables": f'{{"mediaID":"{post_id}"}}',
            "doc_id": "9360915773983802",
        }

        response = self.http_client.post(
            "https://www.threads.net/api/graphql", params=params, headers=headers
        )

        try:
            thread = GetThreadLikersResponse.from_dict(response.json())
            return thread.data.likers
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return UsersData(users=[])

    def __toggle_auth__post_request(self, url: str):
        if self.token is None:
            token = self.get_token()
        else:
            token = self.token
        if token is None:
            raise "Token not found"
        headers = self.__get_app_headers()
        response = self.http_client.post(url, headers=headers)
        return response

    def like(self, post_id: str) -> bool:
        """
        like a post.

        Args:
            post_id (str): post identifier

        Returns:
            boolean and if verbose mode is enabled, prints response dict
        """
        user_id = self.user_id or self.get_current_user_id()
        response = self.__toggle_auth__post_request(
            url=f'{BASE_API_URL}/media/{post_id}_{user_id}/like/',)
        if self.verbose:
            print("[LIKE]", response.json())
        return response.json()["status"] == "ok"

    def unlike(self, post_id: str) -> bool:
        """
        takes your like back from a post.

        Args:
            post_id (str): post identifier

        Returns:
            boolean and if verbose mode is enabled, prints response dict
        """
        user_id = self.user_id or self.get_current_user_id()
        response = self.__toggle_auth__post_request(
            f"{BASE_API_URL}/media/{post_id}_{user_id}/unlike/",)
        if self.verbose:
            print("[UNLIKE]", response.json())
        return response.json()["status"] == "ok"

    def follow(self, user_id: str) -> bool:
        res = self.__toggle_auth__post_request(
            f"{BASE_API_URL}/api/v1/friendships/create/{user_id}/"
        )
        if self.verbose:
            print("[FOLLOW]", res.json())
        return res.json()

    def unfollow(self, user_id: str) -> bool:
        res = self.__toggle_auth__post_request(
            f"{BASE_API_URL}/api/v1/friendships/destroy/{user_id}/"
        )
        if self.verbose:
            print("[UNFOLLOW]", res.json())
        return res.json()

    def get_token(self) -> str:
        """
        set fb login token

        Returns:
            str: validate token string None if not valid
        """
        try:
            blockVersion = (
                "5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73"
            )
            params = json.dumps(
                {
                    "client_input_params": {
                        "password": f"#PWD_INSTAGRAM:4:{self.timestamp_string}:{self.encrypted_password}",
                        "contact_point": self.username,
                        "device_id": self.device_id,
                    },
                    "server_params": {
                        "credential_type": "password",
                        "device_id": self.device_id,
                    },
                },
            )
            bk_client_context = json.dumps(
                {"bloks_version": blockVersion, "styles_id": "instagram"}
            )
            params_quote = quote(string=params, safe="!~*'()")
            bk_client_context_quote = quote(string=bk_client_context, safe="!~*'()")

            response = requests.post(
                url=f"{BASE_API_URL}/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/",
                headers={
                    "User-Agent": "Barcelona 289.0.0.77.109 Android",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                },
                data=f"params={params_quote}&bk_client_context={bk_client_context_quote}&bloks_versioning_id={blockVersion}",
            )

            data = response.text
            if data == "Oops, an error occurred.":
                return None
            pos = data.find("Bearer IGT:2:")
            data_txt = data[pos:]
            backslash_pos = data_txt.find("\\\\")
            token = data_txt[13:backslash_pos]

            return token

        except Exception as e:
            print("[ERROR] ", e)

            return None

    def publish(
        self,
        caption: str,
        image_path: str = None,
        url: str = None,
        parent_post_id: str = None,
    ) -> bool:
        """
        Returns publish post

        Args:
            caption (str): post_id which is unique to each post.
            image_path (str, optional): image_path which is unique to each user.
            url (str, optional): url which is unique to each user.
            parent_post_id (str, optional): parent_post_id which is unique to each user.

        Returns:
            bool: verify that the post went publish
        """
        if self.username is None or self.password is None:
            return False

        user_id = self.get_user_id_from_username(self.username)
        if user_id is None:
            return False
        if self.token is None:
            token = self.get_token()
            if token is not None:
                return False
        now = datetime.now()
        timezone_offset = (datetime.now() - datetime.utcnow()).seconds

        params = {
            "text_post_app_info": {"reply_control": 0},
            "timezone_offset": "-" + str(timezone_offset),
            "source_type": "4",
            "_uid": self.user_id,
            "device_id": str(self.device_id),
            "caption": caption,
            "upload_id": str(int(now.timestamp() * 1000)),
            "device": {
                "manufacturer": "OnePlus",
                "model": "ONEPLUS+A3010",
                "android_version": 25,
                "android_release": "7.1.1",
            },
        }
        post_url = f"{BASE_API_URL}/api/v1/media/configure_text_only_post/"
        if image_path is not None:
            post_url = f"{BASE_API_URL}/api/v1/media/configure_text_post_app_feed/"

            image_content = None
            if not (os.path.isfile(image_path) and os.path.exists(image_path)):
                if not self.__is_valid_url(image_path):
                    return False
                else:
                    image_content = self.__download(image_path)
            upload_id = self.upload_image(
                image_url=image_path, image_content=image_content
            )
            if upload_id == None:
                return False
            params["upload_id"] = upload_id["upload_id"]
            params["scene_capture_type"] = ""
        elif url is not None:
            params["text_post_app_info"]["link_attachment_url"] = url
        if image_path is None:
            params["publish_mode"] = "text_post"

        if parent_post_id is not None:
            params["text_post_app_info"]["reply_id"] = parent_post_id
        params = json.dumps(params)
        payload = f"signed_body=SIGNATURE.{urllib.parse.quote(params)}"
        headers = self.__get_app_headers().copy()
        try:
            response = requests.post(post_url, headers=headers, data=payload)
            if response.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            if self.verbose:
                print("[ERROR] ", e)
            return False

    def publish_with_image(self, caption: str, image_path: str) -> bool:
        """
        @@deprecated
        Returns publish post with image

        Args:
            caption (str): post_id which is unique to each post.
            image_path (str): image path

        Returns:
            bool: verify that the post with image went publish
        """
        return self.publish(caption=caption, image_path=image_path)

    def upload_image(self, image_url: str, image_content: bytes) -> str:
        headers = self.__get_app_headers().copy()

        upload_id = int(time.time() * 1000)
        name = f"{upload_id}_0_{random.randint(1000000000, 9999999999)}"
        url = "https://www.instagram.com/rupload_igphoto/" + name
        mime_type = None
        if image_content is None:
            f = open(image_url, mode="rb")
            content = f.read()
            f.close()
            mime_type, _ = mimetypes.guess_type(image_url)
        else:
            content = image_content
            response = requests.head(image_url)
            content_type = response.headers.get("Content-Type")
            if not content_type:
                file_name = url.split("/")[-1]
                mime_type, _ = mimetypes.guess_type(file_name)
            if mime_type == None:
                mime_type = "jpeg"

        x_instagram_rupload_params = {
            "upload_id": f"{upload_id}",
            "media_type": "1",
            "sticker_burnin_params": "[]",
            "image_compression": json.dumps(
                {"lib_name": "moz", "lib_version": "3.1.m", "quality": "80"}
            ),
            "xsharing_user_ids": "[]",
            "retry_context": {
                "num_step_auto_retry": "0",
                "num_reupload": "0",
                "num_step_manual_retry": "0",
            },
            "IG-FB-Xpost-entry-point-v2": "feed",
        }
        contentLength = len(content)
        if mime_type.startswith("image/"):
            mime_type = mime_type.replace("image/", "")
        image_headers = {
            "X_FB_PHOTO_WATERFALL_ID": str(uuid.uuid4()),
            "X-Entity-Type": "image/" + mime_type,
            "Offset": "0",
            "X-Instagram-Rupload-Params": json.dumps(x_instagram_rupload_params),
            "X-Entity-Name": f"{name}",
            "X-Entity-Length": f"{contentLength}",
            "Content-Type": "application/octet-stream",
            "Content-Length": f"{contentLength}",
            "Accept-Encoding": "gzip",
        }

        headers.update(image_headers)
        response = self.http_client.post(url, headers=headers, data=content)
        if response.status_code == 200:
            return response.json()
        else:
            return None
