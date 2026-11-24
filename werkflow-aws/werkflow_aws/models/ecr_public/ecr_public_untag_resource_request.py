from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
