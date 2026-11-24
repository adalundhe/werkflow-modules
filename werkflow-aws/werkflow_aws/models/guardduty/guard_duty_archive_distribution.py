from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GuardDutyArchiveDistribution(BaseModel):
    ArchivedCount: StrictInt | None = None
    UnarchivedCount: StrictInt | None = None
    ArchivedPercentage: StrictFloat | StrictInt | None = None
    UnarchivedPercentage: StrictFloat | StrictInt | None = None
