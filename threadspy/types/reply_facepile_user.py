from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ReplyFacepileUser:
    # __typename: str
    id: any
    profile_pic_url: str