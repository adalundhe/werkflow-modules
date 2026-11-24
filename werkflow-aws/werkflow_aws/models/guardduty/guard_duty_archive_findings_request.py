from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyArchiveFindingsRequest(BaseModel):
    DetectorId: StrictStr
    FindingIds: list[StrictStr]
