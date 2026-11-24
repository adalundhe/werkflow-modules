from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheNodeGroupConfiguration(BaseModel):
    NodeGroupId: StrictStr | None = None
    Slots: StrictStr | None = None
    ReplicaCount: StrictInt | None = None
    PrimaryAvailabilityZone: StrictStr | None = None
    ReplicaAvailabilityZones: list[StrictStr] | None = None
    PrimaryOutpostArn: StrictStr | None = None
    ReplicaOutpostArns: list[StrictStr] | None = None
