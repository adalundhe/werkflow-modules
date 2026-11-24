from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheConfigureShard(BaseModel):
    NodeGroupId: StrictStr
    NewReplicaCount: StrictInt
    PreferredAvailabilityZones: list[StrictStr] | None = None
    PreferredOutpostArns: list[StrictStr] | None = None
