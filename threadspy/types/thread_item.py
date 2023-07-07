from typing import List
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.post import Post
from threadspy.types.reply_facepile_user import ReplyFacepileUser


@dataclass_json
@dataclass
class ThreadItem:
    post: Post
    line_type: str
    reply_facepile_users: List[ReplyFacepileUser]
    should_show_replies_cta: bool
    # __typename: str
    view_replies_cta_string: str = None
