from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[EndUserMessagingTag]
