from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class BatchNodeDetails(BaseModel):
    nodeIndex: StrictInt | None = None
    isMainNode: StrictBool | None = None
