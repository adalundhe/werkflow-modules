from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
