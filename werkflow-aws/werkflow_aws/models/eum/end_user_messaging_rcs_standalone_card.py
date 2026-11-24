from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .end_user_messaging_rcs_card_content import EndUserMessagingRcsCardContent


class EndUserMessagingRcsStandaloneCard(BaseModel):
    CardOrientation: StrictStr
    CardContent: EndUserMessagingRcsCardContent
    ThumbnailImageAlignment: StrictStr | None = None
