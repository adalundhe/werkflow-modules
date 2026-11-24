from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingListTagsForResourceResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
