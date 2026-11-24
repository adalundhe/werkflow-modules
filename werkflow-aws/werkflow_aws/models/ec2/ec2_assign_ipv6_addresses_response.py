from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2AssignIpv6AddressesResponse(BaseModel):
    AssignedIpv6Addresses: list[StrictStr] | None = None
    AssignedIpv6Prefixes: list[StrictStr] | None = None
    NetworkInterfaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
