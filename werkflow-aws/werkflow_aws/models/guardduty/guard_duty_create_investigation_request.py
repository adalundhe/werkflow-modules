from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCreateInvestigationRequest(BaseModel):
    DetectorId: StrictStr
    TriggerPrompt: StrictStr
    ClientToken: StrictStr | None = None
