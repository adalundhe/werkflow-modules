from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitDeleteCommentContentRequest(BaseModel):
    commentId: StrictStr
