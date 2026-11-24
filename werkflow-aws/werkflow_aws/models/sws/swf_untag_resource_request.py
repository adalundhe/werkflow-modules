from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
