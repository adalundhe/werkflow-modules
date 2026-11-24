from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingUpdateSenderIdRequest(BaseModel):
    SenderId: StrictStr
    IsoCountryCode: StrictStr
    DeletionProtectionEnabled: StrictBool | None = None
