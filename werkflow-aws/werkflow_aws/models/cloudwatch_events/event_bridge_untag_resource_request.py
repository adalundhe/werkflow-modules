from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
