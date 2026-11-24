from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudSearchLimits(BaseModel):
    MaximumReplicationCount: StrictInt | None = None
    MaximumPartitionCount: StrictInt | None = None
