from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
