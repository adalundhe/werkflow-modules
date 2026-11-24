from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsReplyAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
