from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyCoverageStatistics(BaseModel):
    CountByResourceType: dict[StrictStr, StrictInt] | None = None
    CountByCoverageStatus: dict[StrictStr, StrictInt] | None = None
