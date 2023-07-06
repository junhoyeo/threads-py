import requests
import re

class ThreadsAPI:
    fbLSDToken = 'NjppQDEgONsU_1LCzrmp6q' # FIXME: Remove default value

    def __init__(self, options=None):
        if options and 'fbLSDToken' in options:
            self.fbLSDToken = options['fbLSDToken']

    def _get_default_headers(self, username):
        return {
            'authority': 'www.threads.net',
            'accept': '*/*',
            'accept-language': 'ko,en;q=0.9,ko-KR;q=0.8,ja;q=0.7',
            'cache-control': 'no-cache',
            'origin': 'https://www.threads.net',
            'pragma': 'no-cache',
            'referer': f'https://www.threads.net/@{username}',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1',
            'x-asbd-id': '129477',
            'x-fb-lsd': self.fbLSDToken,
            'x-ig-app-id': '238260118697367'
        }

    def get_user_id_from_username(self, username):
        headers = self._get_default_headers(username)
        headers['referer'] = 'https://www.instagram.com/'

        response = requests.get(f'https://www.threads.net/@{username}', headers=headers)
        text = response.text.replace('\n', '')

        user_id = re.search(r'"props":{"user_id":"(\d+)"},', text)
        if user_id:
            return user_id.group(1)
        else:
            return None

    def get_user_profile(self, username, user_id=None):
        """
            Requires username and as an optional parameter user_id.
            If no user_id is passed then the function will automatically get user_id by
            resolving username.
        """
        if not user_id:
            user_id = self.get_user_id_from_username(username)
        headers = self._get_default_headers(username)
        headers['x-fb-friendly-name'] = 'BarcelonaProfileRootQuery'

        params = {
            'av': '0',
            '__user': '0',
            '__a': '1',
            '__req': '1',
            '__hs': '19544.HYP:barcelona_web_pkg.2.1..0.0',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1007795914',
            '__s': 'c1fpxh:oh98tm:os2fqi',
            '__hsi': '7252655495199472548',
            '__dyn': '7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE465o-cw5Mx62G3i0Bo7O2l0Fwqo31wnEfovwRwlE-U2zxe2Gew9O22362W2K0zK5o4q0GpovU1aUbodEGdwtU2ewbS1LwTwNwLw8O1pwr82gxC',
            '__csr': 'j8kjt5p9e00hB4Eqw-w0Xiwrk0xE9Eixza2svazUndhEpko9xy7Ej7Saxl2U5-8m8yA4zCwxxWegQz5162a5x02UxW1g2Ex3MwM_3M25wlQ13gN0el4m2H3r16089wxwnq0w8gqd12',
            '__comet_req': '29',
            'lsd': self.fbLSDToken,
            'jazoest': '21997',
            '__spin_r': '1007795914',
            '__spin_b': 'trunk',
            '__spin_t': '1688640447',
            '__jssesw': '2',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'BarcelonaProfileRootQuery',
            'variables': f'{{"userID":"{user_id}"}}',
            'server_timestamps': 'true',
            'doc_id': '23996318473300828'
        }

        response = requests.post('https://www.threads.net/api/graphql', params=params, headers=headers)
        user = response.json()['data']['userData']['user']
        return user

    def get_user_profile_threads(self, username, user_id=None):
        """
        Returns user profile threads as a dict

        Args:
            username (string): username on threads.net
            user_id (string, optional): user_id which is unique to each user. Defaults to None.

        Returns:
            dict: list of user profile threads.
        """        
        headers = self._get_default_headers(username)
        headers['x-fb-friendly-name'] = 'BarcelonaProfileThreadsTabQuery'

        params = {
            'av': '0',
            '__user': '0',
            '__a': '1',
            '__req': '2',
            '__hs': '19544.HYP:barcelona_web_pkg.2.1..0.0',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1007795914',
            '__s': 'c1fpxh:oh98tm:os2fqi',
            '__hsi': '7252655495199472548',
            '__dyn': '7xeUmwlEnwn8K2WnFw9-2i5U4e0yoW3q32360CEbo1nEhw2nVE4W0om78b87C0yE465o-cw5Mx62G3i0Bo7O2l0Fwqo31wnEfovwRwlE-U2zxe2Gew9O22362W2K0zK5o4q0GpovU1aUbodEGdwtU2ewbS1LwTwNwLw8O1pwr82gxC',
            '__csr': 'j8kjt5p9e00hB4Eqw-w0Xiwrk0xE9Eixza2svazUndhEpko9xy7Ej7Saxl2U5-8m8yA4zCwxxWegQz5162a5x02UxW1g2Ex3MwM_3M25wlQ13gN0el4m2H3r16089wxwnq0w8gqd12',
            '__comet_req': '29',
            'lsd': self.fbLSDToken,
            'jazoest': '21997',
            '__spin_r': '1007795914',
            '__spin_b': 'trunk',
            '__spin_t': '1688640447',
            '__jssesw': '2',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'BarcelonaProfileThreadsTabQuery',
            'variables': f'{{"userID":"{user_id}"}}',
            'server_timestamps': 'true',
            'doc_id': '6232751443445612'
        }

        response = requests.post('https://www.threads.net/api/graphql', params=params, headers=headers)
        threads = response.json()
        print(threads)
        # threads = response.json()['data']['mediaData']['threads']
        return threads
