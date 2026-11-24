from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_attachment_output import QBusinessAttachmentOutput


class QBusinessFailedAttachmentEvent(BaseModel):
    conversationId: StrictStr | None = None
    userMessageId: StrictStr | None = None
    systemMessageId: StrictStr | None = None
    attachment: QBusinessAttachmentOutput | None = None
