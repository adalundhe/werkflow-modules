from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: dict[StrictStr, StrictStr]
