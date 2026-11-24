from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AccessAnalyzerCriterion(BaseModel):
    eq: list[StrictStr] | None = None
    neq: list[StrictStr] | None = None
    contains: list[StrictStr] | None = None
    exists: StrictBool | None = None
