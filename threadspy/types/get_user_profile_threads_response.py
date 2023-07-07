from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.extensions import Extensions
from threadspy.types.common import CommonMediaDataResponse


@dataclass_json
@dataclass
class GetUserProfileThreadsResponse:
    data: CommonMediaDataResponse
    extensions: Extensions
