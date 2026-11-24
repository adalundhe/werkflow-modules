from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_supporting_data import GuardDutySupportingData


class GuardDutyInvestigationRecord(BaseModel):
    RecordId: StrictStr | None = None
    Type: StrictStr | None = None
    Title: StrictStr | None = None
    Narrative: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    SupportingData: GuardDutySupportingData | None = None
