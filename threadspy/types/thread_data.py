from typing import List, Optional
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.thread import Thread


@dataclass_json
@dataclass
class ThreadData:
    reply_threads: List[Thread]
    containing_thread: Optional[Thread] = None
