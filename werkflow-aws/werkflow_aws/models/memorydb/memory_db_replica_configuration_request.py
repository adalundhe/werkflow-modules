from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MemoryDBReplicaConfigurationRequest(BaseModel):
    ReplicaCount: StrictInt | None = None
