from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetConfigurationSetEventDestinationsRequest(BaseModel):
    ConfigurationSetName: StrictStr
