from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_approval import CodeCommitApproval


class CodeCommitGetPullRequestApprovalStatesResponse(BaseModel):
    approvals: list[CodeCommitApproval] | None = None
    ResponseMetadata: dict[str, Any] | None = None
