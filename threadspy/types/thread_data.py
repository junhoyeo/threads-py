from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.thread import Thread


@dataclass_json
@dataclass
class ThreadData:
    containing_thread: Thread
    reply_threads: List[Thread]
