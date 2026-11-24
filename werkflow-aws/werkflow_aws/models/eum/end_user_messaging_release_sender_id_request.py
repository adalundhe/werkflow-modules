from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingReleaseSenderIdRequest(BaseModel):
    SenderId: StrictStr
    IsoCountryCode: StrictStr
