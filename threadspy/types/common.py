from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.users import UsersData
from threadspy.types.media_data import MediaData
from threadspy.types.thread_data import ThreadData
from threadspy.types.user_profile_data import UserProfileData


@dataclass_json
@dataclass
class CommonMediaDataResponse:
    mediaData: MediaData


@dataclass_json
@dataclass
class CommonThreadDataResponse:
    data: ThreadData


@dataclass_json
@dataclass
class CommonUserProfileDataResponse:
    data: UserProfileData


@dataclass_json
@dataclass
class CommonLikersResponse:
    likers: UsersData
