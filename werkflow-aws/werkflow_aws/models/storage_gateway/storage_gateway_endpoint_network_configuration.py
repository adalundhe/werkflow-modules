from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayEndpointNetworkConfiguration(BaseModel):
    IpAddresses: list[StrictStr] | None = None
