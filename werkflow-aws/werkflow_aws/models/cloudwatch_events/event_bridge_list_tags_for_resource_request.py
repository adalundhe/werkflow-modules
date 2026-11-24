from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
