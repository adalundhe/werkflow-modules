from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitPutCommentReactionRequest(BaseModel):
    commentId: StrictStr
    reactionValue: StrictStr
