from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPrepSimpleAggregationFunction(BaseModel):
    InputColumnName: StrictStr | None = None
    FunctionType: StrictStr | None = None
