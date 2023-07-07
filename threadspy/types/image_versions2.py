from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.candidate import Candidate


@dataclass_json
@dataclass
class ImageVersions2:
    candidates: List[Candidate]
