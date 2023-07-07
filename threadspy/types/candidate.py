from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Candidate:
    height: int
    url: str
    width: int
    # __typename: str