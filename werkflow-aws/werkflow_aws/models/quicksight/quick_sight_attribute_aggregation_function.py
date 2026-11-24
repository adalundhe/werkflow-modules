from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAttributeAggregationFunction(BaseModel):
    SimpleAttributeAggregation: StrictStr | None = None
    ValueForMultipleValues: StrictStr | None = None
