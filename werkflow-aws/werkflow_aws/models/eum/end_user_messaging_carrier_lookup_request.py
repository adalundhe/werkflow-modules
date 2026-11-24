from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingCarrierLookupRequest(BaseModel):
    PhoneNumber: StrictStr
    EnableCleansing: StrictBool | None = None
