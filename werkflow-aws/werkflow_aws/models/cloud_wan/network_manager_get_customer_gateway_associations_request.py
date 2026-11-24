from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerGetCustomerGatewayAssociationsRequest(BaseModel):
    GlobalNetworkId: StrictStr
    CustomerGatewayArns: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
