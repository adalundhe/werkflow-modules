from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
