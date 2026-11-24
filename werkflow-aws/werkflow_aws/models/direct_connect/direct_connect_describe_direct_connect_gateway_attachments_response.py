from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_gateway_attachment import DirectConnectGatewayAttachment


class DirectConnectDescribeDirectConnectGatewayAttachmentsResponse(BaseModel):
    directConnectGatewayAttachments: list[DirectConnectGatewayAttachment] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
