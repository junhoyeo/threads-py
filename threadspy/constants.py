import hashlib
import time

DEFAULT_LSD_TOKEN = "NjppQDEgONsU_1LCzrmp6q"
DEFAULT_DEVICE_ID = (
    f"android-${hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]}"
)
LATEST_ANDROID_APP_VERSION = "289.0.0.77.109"
BASE_API_URL = "https://i.instagram.com"
