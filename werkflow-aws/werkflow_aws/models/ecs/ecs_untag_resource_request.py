from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
