from __future__ import annotations
from pydantic import BaseModel
from .end_user_messaging_rcs_carousel import EndUserMessagingRcsCarousel
from .end_user_messaging_rcs_file_message import EndUserMessagingRcsFileMessage
from .end_user_messaging_rcs_standalone_card import EndUserMessagingRcsStandaloneCard
from .end_user_messaging_rcs_text_message import EndUserMessagingRcsTextMessage


class EndUserMessagingRcsContent(BaseModel):
    TextMessage: EndUserMessagingRcsTextMessage | None = None
    FileMessage: EndUserMessagingRcsFileMessage | None = None
    RichCard: EndUserMessagingRcsStandaloneCard | None = None
    Carousel: EndUserMessagingRcsCarousel | None = None
