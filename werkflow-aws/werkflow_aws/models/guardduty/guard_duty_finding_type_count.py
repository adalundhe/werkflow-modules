from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyFindingTypeCount(BaseModel):
    FindingType: StrictStr | None = None
    Count: StrictInt | None = None
