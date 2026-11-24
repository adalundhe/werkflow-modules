from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_gateway_association_proposal import DirectConnectGatewayAssociationProposal


class DirectConnectDeleteDirectConnectGatewayAssociationProposalResponse(BaseModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposal | None = None
    ResponseMetadata: dict[str, Any] | None = None
