from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsDialPhoneAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
    PhoneNumber: StrictStr
