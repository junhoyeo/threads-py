import random

DEFAULT_LSD_TOKEN = "NjppQDEgONsU_1LCzrmp6q"
DEFAULT_DEVICE_ID = f"android-{random.randint(0, 1e24):x}"
POST_HEADERS_DEFAULT = {
    "User-Agent": "Barcelona 289.0.0.77.109 Android",
    "Sec-Fetch-Site": "same-origin",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}
BASE_API_URL = "https://i.instagram.com/api/v1"
LOGIN_URL = BASE_API_URL + "/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"
POST_URL = BASE_API_URL + "/media/configure_text_only_post/"
POST_WITH_IMAGE_URL = BASE_API_URL + "/media/configure_text_post_app_feed/"
UPDATE_MEDIA_PQD_HASH_URL = BASE_API_URL + "/media/update_media_with_pdq_hash_info/"
