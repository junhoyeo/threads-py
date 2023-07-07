from typing import List, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from threadspy.types.caption import Caption
from threadspy.types.image_versions2 import ImageVersions2
from threadspy.types.text_post_app_info import TextPostAppInfo
from threadspy.types.threads_user_summary import ThreadsUserSummary


@dataclass_json
@dataclass
class Post:
    user: ThreadsUserSummary
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    video_versions: List[Any]
    carousel_media: Any
    carousel_media_count: Any
    pk: str
    has_audio: Any
    text_post_app_info: TextPostAppInfo
    taken_at: int
    like_count: int
    code: str
    media_overlay_info: Any
    id: str
    caption: Caption = None
