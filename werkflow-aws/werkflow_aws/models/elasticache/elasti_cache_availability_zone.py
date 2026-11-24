from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
