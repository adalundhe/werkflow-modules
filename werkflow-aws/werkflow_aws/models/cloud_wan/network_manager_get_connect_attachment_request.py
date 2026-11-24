from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetConnectAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
