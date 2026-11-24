from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_branch_info import CodeCommitBranchInfo


class CodeCommitGetBranchResponse(BaseModel):
    branch: CodeCommitBranchInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
