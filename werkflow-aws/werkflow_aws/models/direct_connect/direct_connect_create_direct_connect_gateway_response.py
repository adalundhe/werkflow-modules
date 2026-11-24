from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_gateway import DirectConnectGateway


class DirectConnectCreateDirectConnectGatewayResponse(BaseModel):
    directConnectGateway: DirectConnectGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None
