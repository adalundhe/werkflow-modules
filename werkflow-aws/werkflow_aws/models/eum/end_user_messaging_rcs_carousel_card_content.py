from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_rcs_carousel_card_media import EndUserMessagingRcsCarouselCardMedia
from .end_user_messaging_rcs_suggested_action import EndUserMessagingRcsSuggestedAction


class EndUserMessagingRcsCarouselCardContent(BaseModel):
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Media: EndUserMessagingRcsCarouselCardMedia | None = None
    Suggestions: list[EndUserMessagingRcsSuggestedAction] | None = None
