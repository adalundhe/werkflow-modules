from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2UntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
