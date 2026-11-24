from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationDetectorFeatureConfiguration(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
