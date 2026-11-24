from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetDirectConnectGatewayAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
