from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteEventDestinationRequest(BaseModel):
    ConfigurationSetName: StrictStr
    EventDestinationName: StrictStr
