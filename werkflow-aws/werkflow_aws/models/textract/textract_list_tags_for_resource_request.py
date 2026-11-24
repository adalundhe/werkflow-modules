from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
