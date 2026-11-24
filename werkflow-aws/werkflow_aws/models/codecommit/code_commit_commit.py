from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_user_info import CodeCommitUserInfo


class CodeCommitCommit(BaseModel):
    commitId: StrictStr | None = None
    treeId: StrictStr | None = None
    parents: list[StrictStr] | None = None
    message: StrictStr | None = None
    author: CodeCommitUserInfo | None = None
    committer: CodeCommitUserInfo | None = None
    additionalData: StrictStr | None = None
