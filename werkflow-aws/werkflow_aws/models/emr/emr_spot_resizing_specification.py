from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRSpotResizingSpecification(BaseModel):
    TimeoutDurationMinutes: StrictInt | None = None
    AllocationStrategy: StrictStr | None = None
