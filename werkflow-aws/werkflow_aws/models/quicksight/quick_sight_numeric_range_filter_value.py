from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightNumericRangeFilterValue(BaseModel):
    StaticValue: StrictFloat | StrictInt | None = None
    Parameter: StrictStr | None = None
