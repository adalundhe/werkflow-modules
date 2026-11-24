from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_direct_connect_gateway_attachment import NetworkManagerDirectConnectGatewayAttachment


class NetworkManagerCreateDirectConnectGatewayAttachmentResponse(BaseModel):
    DirectConnectGatewayAttachment: NetworkManagerDirectConnectGatewayAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
