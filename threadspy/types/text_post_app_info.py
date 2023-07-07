from typing import Any, Optional
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TextPostAppInfo:
    link_preview_attachment: Any
    share_info: Any
    reply_to_author: Any
    is_post_unavailable: bool
    direct_reply_count: Optional[int] = 0
