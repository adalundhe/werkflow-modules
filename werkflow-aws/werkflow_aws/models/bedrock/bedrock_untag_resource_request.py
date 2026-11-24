from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockUntagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tagKeys: list[StrictStr]
