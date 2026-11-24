from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateCommentRequest(BaseModel):
    commentId: StrictStr
    content: StrictStr
