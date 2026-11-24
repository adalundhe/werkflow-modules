from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2PublicIpv4PoolRange(BaseModel):
    FirstAddress: StrictStr | None = None
    LastAddress: StrictStr | None = None
    AddressCount: StrictInt | None = None
    AvailableAddressCount: StrictInt | None = None
