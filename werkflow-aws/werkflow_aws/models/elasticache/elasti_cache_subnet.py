from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_availability_zone import ElastiCacheAvailabilityZone
from .elasti_cache_subnet_outpost import ElastiCacheSubnetOutpost


class ElastiCacheSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: ElastiCacheAvailabilityZone | None = None
    SubnetOutpost: ElastiCacheSubnetOutpost | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
