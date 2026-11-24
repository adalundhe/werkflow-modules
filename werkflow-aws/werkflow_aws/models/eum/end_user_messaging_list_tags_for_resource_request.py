from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
