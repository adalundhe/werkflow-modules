from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCoverageFilterCondition(BaseModel):
    Equals: list[StrictStr] | None = None
    NotEquals: list[StrictStr] | None = None
