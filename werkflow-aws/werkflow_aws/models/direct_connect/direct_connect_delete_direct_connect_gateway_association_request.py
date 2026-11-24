from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteDirectConnectGatewayAssociationRequest(BaseModel):
    associationId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
    virtualGatewayId: StrictStr | None = None
