from __future__ import annotations
from pydantic import BaseModel
from .end_user_messaging_rcs_content import EndUserMessagingRcsContent
from .end_user_messaging_rcs_suggested_action import EndUserMessagingRcsSuggestedAction


class EndUserMessagingRcsMessageContent(BaseModel):
    Content: EndUserMessagingRcsContent
    Suggestions: list[EndUserMessagingRcsSuggestedAction] | None = None
