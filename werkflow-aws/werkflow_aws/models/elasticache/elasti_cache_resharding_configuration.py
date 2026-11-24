from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheReshardingConfiguration(BaseModel):
    NodeGroupId: StrictStr | None = None
    PreferredAvailabilityZones: list[StrictStr] | None = None
