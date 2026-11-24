from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteConfigurationSetEventDestinationRequest(BaseModel):
    ConfigurationSetName: StrictStr
    EventDestinationName: StrictStr
