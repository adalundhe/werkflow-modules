from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayEndpointConfiguration(BaseModel):
    types: list[StrictStr] | None = None
    ipAddressType: StrictStr | None = None
    vpcEndpointIds: list[StrictStr] | None = None
