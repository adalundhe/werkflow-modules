from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchArrayPropertiesDetail(BaseModel):
    statusSummary: dict[StrictStr, StrictInt] | None = None
    statusSummaryLastUpdatedAt: StrictInt | None = None
    size: StrictInt | None = None
    index: StrictInt | None = None
