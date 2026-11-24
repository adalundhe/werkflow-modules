from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBShardConfiguration(BaseModel):
    Slots: StrictStr | None = None
    ReplicaCount: StrictInt | None = None
