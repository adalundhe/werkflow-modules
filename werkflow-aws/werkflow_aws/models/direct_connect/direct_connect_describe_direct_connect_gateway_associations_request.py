from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectDescribeDirectConnectGatewayAssociationsRequest(BaseModel):
    associationId: StrictStr | None = None
    associatedGatewayId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    virtualGatewayId: StrictStr | None = None
