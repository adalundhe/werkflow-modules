from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class OpenSearchServerlessCollectionGroupCapacityLimits(BaseModel):
    maxIndexingCapacityInOCU: StrictFloat | StrictInt | None = None
    maxSearchCapacityInOCU: StrictFloat | StrictInt | None = None
    minIndexingCapacityInOCU: StrictFloat | StrictInt | None = None
    minSearchCapacityInOCU: StrictFloat | StrictInt | None = None
