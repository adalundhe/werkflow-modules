from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_gateway_association import DirectConnectGatewayAssociation


class DirectConnectAcceptDirectConnectGatewayAssociationProposalResponse(BaseModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
