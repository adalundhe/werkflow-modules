from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
