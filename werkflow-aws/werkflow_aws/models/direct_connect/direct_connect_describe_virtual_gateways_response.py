from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_virtual_gateway import DirectConnectVirtualGateway


class DirectConnectDescribeVirtualGatewaysResponse(BaseModel):
    virtualGateways: list[DirectConnectVirtualGateway] | None = None
    ResponseMetadata: dict[str, Any] | None = None
