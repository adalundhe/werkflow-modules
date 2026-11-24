from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaCapacityAssignment(BaseModel):
    WorkGroupNames: list[StrictStr] | None = None
