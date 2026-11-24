from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataAggregation(BaseModel):
    DatasetRowDateGranularity: StrictStr | None = None
    DefaultDateColumnName: StrictStr | None = None
