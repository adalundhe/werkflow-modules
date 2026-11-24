from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudTrailQueryStatistics(BaseModel):
    ResultsCount: StrictInt | None = None
    TotalResultsCount: StrictInt | None = None
    BytesScanned: StrictInt | None = None
