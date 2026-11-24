from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetTransitGatewayRouteTableAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
