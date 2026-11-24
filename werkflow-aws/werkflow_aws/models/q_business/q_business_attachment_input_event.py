from __future__ import annotations
from pydantic import BaseModel
from .q_business_attachment_input import QBusinessAttachmentInput


class QBusinessAttachmentInputEvent(BaseModel):
    attachment: QBusinessAttachmentInput | None = None
