from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_reaction_for_comment import CodeCommitReactionForComment


class CodeCommitGetCommentReactionsResponse(BaseModel):
    reactionsForComment: list[CodeCommitReactionForComment] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
