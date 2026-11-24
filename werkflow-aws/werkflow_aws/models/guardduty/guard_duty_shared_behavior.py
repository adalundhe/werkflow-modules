from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutySharedBehavior(BaseModel):
    Path: StrictStr | None = None
    Value: StrictStr | None = None
