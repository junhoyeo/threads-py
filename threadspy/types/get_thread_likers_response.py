from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.extensions import Extensions
from threadspy.types.common import CommonLikersResponse


@dataclass_json
@dataclass
class GetThreadLikersResponse:
    data: CommonLikersResponse
    extensions: Extensions
