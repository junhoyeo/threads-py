import hashlib
import time

DEFAULT_LSD_TOKEN = "NjppQDEgONsU_1LCzrmp6q"
DEFAULT_DEVICE_ID = 'android-%s' % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
LATEST_ANDROID_APP_VERSION = "289.0.0.77.109"
BASE_API_URL = "https://i.instagram.com/api/v1"
LOGIN_URL = BASE_API_URL + "/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"
POST_URL = BASE_API_URL + "/media/configure_text_only_post/"
POST_WITH_IMAGE_URL = BASE_API_URL + "/media/configure_text_post_app_feed/"
UPDATE_MEDIA_PQD_HASH_URL = BASE_API_URL + "/media/update_media_with_pdq_hash_info/"