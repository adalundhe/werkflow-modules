from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_gateway import DirectConnectGateway


class DirectConnectDescribeDirectConnectGatewaysResponse(BaseModel):
    directConnectGateways: list[DirectConnectGateway] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
