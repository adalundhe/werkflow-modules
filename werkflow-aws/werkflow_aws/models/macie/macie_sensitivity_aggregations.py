from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieSensitivityAggregations(BaseModel):
    classifiableSizeInBytes: StrictInt | None = None
    publiclyAccessibleCount: StrictInt | None = None
    totalCount: StrictInt | None = None
    totalSizeInBytes: StrictInt | None = None
