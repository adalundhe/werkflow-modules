from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyUnarchiveFindingsRequest(BaseModel):
    DetectorId: StrictStr
    FindingIds: list[StrictStr]
