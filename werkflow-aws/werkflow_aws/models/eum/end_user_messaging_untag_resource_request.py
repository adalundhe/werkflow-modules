from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
