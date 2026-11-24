from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitGetCommentReactionsRequest(BaseModel):
    commentId: StrictStr
    reactionUserArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
