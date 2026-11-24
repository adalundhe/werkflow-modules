from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
