from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsRequestLocationAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
