from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class WAFv2RevenuePathStatistics(BaseModel):
    Path: StrictStr | None = None
    Percentage: StrictFloat | StrictInt | None = None
    Amount: StrictStr | None = None
    RequestCount: StrictInt | None = None
