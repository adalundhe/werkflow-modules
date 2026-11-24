from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyFindingReference(BaseModel):
    FindingType: StrictStr | None = None
    Uid: StrictStr | None = None
