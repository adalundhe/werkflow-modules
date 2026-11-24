from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
