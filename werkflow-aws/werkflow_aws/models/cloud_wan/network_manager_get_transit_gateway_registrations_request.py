from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetTransitGatewayRegistrationsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayArns: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
