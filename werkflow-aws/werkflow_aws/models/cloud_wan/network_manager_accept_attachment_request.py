from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAcceptAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
