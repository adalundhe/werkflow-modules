from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2AllocateAddressResponse(BaseModel):
    AllocationId: StrictStr | None = None
    PublicIpv4Pool: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    Domain: StrictStr | None = None
    CustomerOwnedIp: StrictStr | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    CarrierIp: StrictStr | None = None
    PublicIp: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
