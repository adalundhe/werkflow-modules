from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
