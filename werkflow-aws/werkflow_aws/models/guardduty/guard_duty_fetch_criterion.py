from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyFetchCriterion(BaseModel):
    Field: StrictStr | None = None
    Condition: StrictStr | None = None
    Values: list[StrictStr] | None = None
