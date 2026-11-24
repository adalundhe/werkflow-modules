from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightDataPrepListAggregationFunction(BaseModel):
    InputColumnName: StrictStr | None = None
    Separator: StrictStr | None = None
    Distinct: StrictBool | None = None
