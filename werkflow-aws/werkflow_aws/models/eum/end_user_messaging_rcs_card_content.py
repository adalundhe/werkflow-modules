from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_rcs_card_media import EndUserMessagingRcsCardMedia
from .end_user_messaging_rcs_suggested_action import EndUserMessagingRcsSuggestedAction


class EndUserMessagingRcsCardContent(BaseModel):
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Media: EndUserMessagingRcsCardMedia | None = None
    Suggestions: list[EndUserMessagingRcsSuggestedAction] | None = None
