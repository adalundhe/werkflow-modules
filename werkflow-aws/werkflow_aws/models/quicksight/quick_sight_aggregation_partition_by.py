from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAggregationPartitionBy(BaseModel):
    FieldName: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
