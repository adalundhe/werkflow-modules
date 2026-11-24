from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GuardDutyGetInvestigationRequest(BaseModel):
    DetectorId: StrictStr
    InvestigationId: StrictStr
    SummaryFormat: Literal['STRING', 'STRUCTURED'] | None = None
