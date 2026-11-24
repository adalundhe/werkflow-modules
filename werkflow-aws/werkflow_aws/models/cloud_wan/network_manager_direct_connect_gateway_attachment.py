from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_attachment import NetworkManagerAttachment


class NetworkManagerDirectConnectGatewayAttachment(BaseModel):
    Attachment: NetworkManagerAttachment | None = None
    DirectConnectGatewayArn: StrictStr | None = None
