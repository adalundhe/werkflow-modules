from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayNetworkInterface(BaseModel):
    Ipv4Address: StrictStr | None = None
    MacAddress: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
