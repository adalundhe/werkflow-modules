from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESPutConfigurationSetSendingOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    SendingEnabled: StrictBool | None = None
