from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_target import CodeCommitTarget


class CodeCommitCreatePullRequestRequest(BaseModel):
    title: StrictStr
    targets: list[CodeCommitTarget]
    description: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
