from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyTotal(BaseModel):
    Amount: StrictStr | None = None
    Unit: StrictStr | None = None
