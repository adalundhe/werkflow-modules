from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_gateway_association import DirectConnectGatewayAssociation


class DirectConnectDescribeDirectConnectGatewayAssociationsResponse(BaseModel):
    directConnectGatewayAssociations: list[DirectConnectGatewayAssociation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
