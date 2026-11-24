from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_availability_zone import MemoryDBAvailabilityZone


class MemoryDBSubnet(BaseModel):
    Identifier: StrictStr | None = None
    AvailabilityZone: MemoryDBAvailabilityZone | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
