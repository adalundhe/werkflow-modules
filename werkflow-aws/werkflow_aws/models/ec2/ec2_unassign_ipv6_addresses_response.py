from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2UnassignIpv6AddressesResponse(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
    UnassignedIpv6Addresses: list[StrictStr] | None = None
    UnassignedIpv6Prefixes: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
