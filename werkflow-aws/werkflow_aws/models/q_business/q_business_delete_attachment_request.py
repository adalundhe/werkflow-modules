from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteAttachmentRequest(BaseModel):
    applicationId: StrictStr
    conversationId: StrictStr
    attachmentId: StrictStr
    userId: StrictStr | None = None
