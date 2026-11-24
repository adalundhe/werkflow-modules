from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectDescribeDirectConnectGatewayAssociationProposalsRequest(BaseModel):
    directConnectGatewayId: StrictStr | None = None
    proposalId: StrictStr | None = None
    associatedGatewayId: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
