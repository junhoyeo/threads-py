from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.extensions import Extensions
from threadspy.types.common import CommonMediaDataResponse


@dataclass_json
@dataclass
class GetUserProfileRepliesResponse:
    data: CommonMediaDataResponse
    extensions: Extensions
