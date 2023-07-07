from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.user_data import UserData


@dataclass_json
@dataclass
class UserProfileData:
    userData: UserData
