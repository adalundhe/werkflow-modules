from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightComparativeOrder(BaseModel):
    UseOrdering: StrictStr | None = None
    SpecifedOrder: list[StrictStr] | None = None
    TreatUndefinedSpecifiedValues: StrictStr | None = None
