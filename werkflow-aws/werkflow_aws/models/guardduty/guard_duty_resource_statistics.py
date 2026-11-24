from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyResourceStatistics(BaseModel):
    AccountId: StrictStr | None = None
    LastGeneratedAt: datetime.datetime | StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    TotalFindings: StrictInt | None = None
