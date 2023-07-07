from typing import List, Any, Optional
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.threads_bio_link import ThreadsBioLink
from threadspy.types.threads_hd_profile_pic_version import ThreadsHdProfilePicVersion


@dataclass_json
@dataclass
class ThreadsUser:
    pk: str
    full_name: str
    profile_pic_url: str
    follower_count: int
    is_verified: bool
    username: str
    profile_context_facepile_users: Any
    id: Any
    hd_profile_pic_versions: Optional[List[ThreadsHdProfilePicVersion]] = None
    biography: Optional[str] = None
    biography_with_entities: Any = None
    bio_links: Optional[List[ThreadsBioLink]] = None
    is_private: Optional[bool] = None
