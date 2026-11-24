from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tags: dict[StrictStr, StrictStr]
