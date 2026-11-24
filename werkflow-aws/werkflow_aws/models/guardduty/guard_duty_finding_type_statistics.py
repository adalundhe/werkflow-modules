from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyFindingTypeStatistics(BaseModel):
    FindingType: StrictStr | None = None
    LastGeneratedAt: datetime.datetime | StrictStr | None = None
    TotalFindings: StrictInt | None = None
