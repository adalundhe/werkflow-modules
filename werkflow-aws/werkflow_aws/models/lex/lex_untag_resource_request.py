from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUntagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tagKeys: list[StrictStr]
