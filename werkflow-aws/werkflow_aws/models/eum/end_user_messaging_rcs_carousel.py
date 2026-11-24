from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_rcs_carousel_card_content import EndUserMessagingRcsCarouselCardContent


class EndUserMessagingRcsCarousel(BaseModel):
    CardWidth: StrictStr
    CardContents: list[EndUserMessagingRcsCarouselCardContent]
