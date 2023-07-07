from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from threadspy.types.caption import Caption
from threadspy.types.video_version import VideoVersion
from threadspy.types.image_versions2 import ImageVersions2
from threadspy.types.text_post_app_info import TextPostAppInfo
from threadspy.types.threads_user_summary import ThreadsUserSummary


@dataclass_json
@dataclass
class RepostedPost:
    pk: str
    user: ThreadsUserSummary
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    video_versions: List[VideoVersion]
    carousel_media: any
    carousel_media_count: any
    text_post_app_info: TextPostAppInfo
    caption: Caption
    like_count: int
    taken_at: int
    code: str
    id: str
    has_audio: bool = None
