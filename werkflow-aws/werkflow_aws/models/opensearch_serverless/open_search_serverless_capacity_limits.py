from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchServerlessCapacityLimits(BaseModel):
    maxIndexingCapacityInOCU: StrictInt | None = None
    maxSearchCapacityInOCU: StrictInt | None = None
