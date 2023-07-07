from typing import List, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.thread_item import ThreadItem


@dataclass_json
@dataclass
class Thread:
    id: str
    thread_items: List[ThreadItem]
    thread_type: str = None
    header: Any = None
