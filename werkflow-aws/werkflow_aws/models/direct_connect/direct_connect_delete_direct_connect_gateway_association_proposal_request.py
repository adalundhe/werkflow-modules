from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteDirectConnectGatewayAssociationProposalRequest(BaseModel):
    proposalId: StrictStr
