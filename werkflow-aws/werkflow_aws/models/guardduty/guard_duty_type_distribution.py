from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutyTypeDistribution(BaseModel):
    FindingType: StrictStr | None = None
    Count: StrictInt | None = None
    Percentage: StrictFloat | StrictInt | None = None
    DominantSeverity: StrictStr | None = None
