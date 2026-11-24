from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_comments_for_compared_commit import CodeCommitCommentsForComparedCommit


class CodeCommitGetCommentsForComparedCommitResponse(BaseModel):
    commentsForComparedCommitData: list[CodeCommitCommentsForComparedCommit] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
