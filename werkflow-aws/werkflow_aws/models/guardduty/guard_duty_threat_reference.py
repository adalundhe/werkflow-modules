from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyThreatReference(BaseModel):
    Name: StrictStr | None = None
    Uid: StrictStr | None = None
