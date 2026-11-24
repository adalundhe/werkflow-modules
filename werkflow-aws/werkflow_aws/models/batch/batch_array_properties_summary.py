from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchArrayPropertiesSummary(BaseModel):
    size: StrictInt | None = None
    index: StrictInt | None = None
    statusSummary: dict[StrictStr, StrictInt] | None = None
    statusSummaryLastUpdatedAt: StrictInt | None = None
