from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeleteAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
