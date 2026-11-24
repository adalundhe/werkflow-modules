from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerUpdateDirectConnectGatewayAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
    EdgeLocations: list[StrictStr] | None = None
