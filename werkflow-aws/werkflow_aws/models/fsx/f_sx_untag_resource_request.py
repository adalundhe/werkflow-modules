from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
