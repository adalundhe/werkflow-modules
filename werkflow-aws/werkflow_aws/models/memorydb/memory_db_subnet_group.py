from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_subnet import MemoryDBSubnet


class MemoryDBSubnetGroup(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    VpcId: StrictStr | None = None
    Subnets: list[MemoryDBSubnet] | None = None
    ARN: StrictStr | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
