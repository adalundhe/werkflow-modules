from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppFlowAggregationConfig(BaseModel):
    aggregationType: StrictStr | None = None
    targetFileSize: StrictInt | None = None
