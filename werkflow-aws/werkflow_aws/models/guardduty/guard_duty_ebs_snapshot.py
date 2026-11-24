from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEbsSnapshot(BaseModel):
    DeviceName: StrictStr | None = None
