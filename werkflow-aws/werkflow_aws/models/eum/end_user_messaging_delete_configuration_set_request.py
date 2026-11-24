from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingDeleteConfigurationSetRequest(BaseModel):
    ConfigurationSetName: StrictStr
