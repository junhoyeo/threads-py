from dataclasses import dataclass
from dataclasses_json import dataclass_json
from threadspy.types.quoted_post import QuotedPost
from threadspy.types.reposted_post import RepostedPost


@dataclass_json
@dataclass
class ShareInfo:
    quoted_post: QuotedPost = None
    reposted_post: RepostedPost = None
