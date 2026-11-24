from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockListTagsForResourceRequest(BaseModel):
    resourceARN: StrictStr
