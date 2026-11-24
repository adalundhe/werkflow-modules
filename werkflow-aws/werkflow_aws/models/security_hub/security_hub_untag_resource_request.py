from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
