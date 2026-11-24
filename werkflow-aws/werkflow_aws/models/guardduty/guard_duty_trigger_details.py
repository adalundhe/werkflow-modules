from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyTriggerDetails(BaseModel):
    GuardDutyFindingId: StrictStr | None = None
    Description: StrictStr | None = None
    TriggerType: StrictStr | None = None
