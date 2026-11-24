from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
