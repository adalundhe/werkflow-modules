from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportAttachmentDetails(BaseModel):
    attachmentId: StrictStr | None = None
    fileName: StrictStr | None = None
