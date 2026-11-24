from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexListTagsForResourceRequest(BaseModel):
    resourceARN: StrictStr
