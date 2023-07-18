from typing import List, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class FriendshipStatus:
    following: bool
    followed_by: bool
    blocking: bool
    muting: bool
    is_private: bool
    incoming_request: bool
    outgoing_request: bool
    text_post_app_pre_following: bool
    is_bestie: bool
    is_restricted: bool
    is_feed_favorite: bool


@dataclass_json
@dataclass
class ProfileContextFacepileUser:
    pk: int
    pk_id: str
    username: str
    full_name: str
    is_private: bool
    is_verified: bool
    profile_pic_id: str
    profile_pic_url: str
    has_onboarded_to_text_post_app: bool


@dataclass_json
@dataclass
class SuggestedUser:
    pk: int
    pk_id: str
    username: str
    full_name: str
    account_badges: List[Any]
    profile_pic_url: str
    has_anonymous_profile_picture: bool
    has_onboarded_to_text_post_app: bool
    is_verified: bool
    friendship_status: FriendshipStatus
    profile_context_facepile_users: List[ProfileContextFacepileUser]
    follower_count: int
