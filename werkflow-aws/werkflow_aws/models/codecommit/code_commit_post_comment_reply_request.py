from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitPostCommentReplyRequest(BaseModel):
    inReplyTo: StrictStr
    content: StrictStr
    clientRequestToken: StrictStr | None = None
