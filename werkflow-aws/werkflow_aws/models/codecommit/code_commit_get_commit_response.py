from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_commit import CodeCommitCommit


class CodeCommitGetCommitResponse(BaseModel):
    commit: CodeCommitCommit | None = None
    ResponseMetadata: dict[str, Any] | None = None
