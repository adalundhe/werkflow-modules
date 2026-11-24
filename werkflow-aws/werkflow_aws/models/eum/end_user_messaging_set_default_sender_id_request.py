from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSetDefaultSenderIdRequest(BaseModel):
    ConfigurationSetName: StrictStr
    SenderId: StrictStr
