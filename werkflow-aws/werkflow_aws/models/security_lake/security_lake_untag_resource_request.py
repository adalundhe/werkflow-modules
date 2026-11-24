from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
