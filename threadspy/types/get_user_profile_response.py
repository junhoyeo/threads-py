from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.extensions import Extensions
from threadspy.types.user_profile_data import UserProfileData


@dataclass_json
@dataclass
class GetUserProfileResponse:
    data: UserProfileData
    extensions: Extensions
