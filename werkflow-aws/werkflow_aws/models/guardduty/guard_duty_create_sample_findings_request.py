from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCreateSampleFindingsRequest(BaseModel):
    DetectorId: StrictStr
    FindingTypes: list[StrictStr] | None = None
