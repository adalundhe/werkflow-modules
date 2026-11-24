from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetTransitGatewayConnectPeerAssociationsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayConnectPeerArns: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
