from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
