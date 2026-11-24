from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
