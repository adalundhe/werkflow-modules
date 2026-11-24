from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyFilterCondition(BaseModel):
    EqualsValue: StrictStr | None = None
    GreaterThan: StrictInt | None = None
    LessThan: StrictInt | None = None
