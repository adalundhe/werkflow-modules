from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class BatchNodePropertiesSummary(BaseModel):
    isMainNode: StrictBool | None = None
    numNodes: StrictInt | None = None
    nodeIndex: StrictInt | None = None
