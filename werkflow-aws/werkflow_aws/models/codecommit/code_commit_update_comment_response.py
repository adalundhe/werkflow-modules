from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_commit_comment import CodeCommitComment


class CodeCommitUpdateCommentResponse(BaseModel):
    comment: CodeCommitComment | None = None
    ResponseMetadata: dict[str, Any] | None = None
