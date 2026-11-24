from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRejectAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
