from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessAttachmentOutput(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    attachmentId: StrictStr | None = None
    conversationId: StrictStr | None = None
