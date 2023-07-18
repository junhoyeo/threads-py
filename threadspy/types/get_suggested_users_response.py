from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.suggested_user import SuggestedUser


@dataclass_json
@dataclass
class GetSuggestedUsersResponse:
    users: List[SuggestedUser]
    paging_token: str
    has_more: bool
    status: str
