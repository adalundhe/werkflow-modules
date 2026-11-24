from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEbsVolumesResult(BaseModel):
    Status: StrictStr | None = None
    Reason: StrictStr | None = None
