from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.extensions import Extensions
from threadspy.types.common import CommonThreadDataResponse


@dataclass_json
@dataclass
class GetUserProfileThreadResponse:
    data: CommonThreadDataResponse
    extensions: Extensions
