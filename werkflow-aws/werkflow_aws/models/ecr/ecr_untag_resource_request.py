from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
