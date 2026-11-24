from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetMediaRequest(BaseModel):
    applicationId: StrictStr
    conversationId: StrictStr
    messageId: StrictStr
    mediaId: StrictStr
