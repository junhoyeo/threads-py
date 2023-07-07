from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ThreadsUserSummary:
    profile_pic_url: str
    username: str
    id: any
    is_verified: bool
    pk: str
