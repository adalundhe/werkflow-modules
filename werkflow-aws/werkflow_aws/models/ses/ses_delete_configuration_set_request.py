from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteConfigurationSetRequest(BaseModel):
    ConfigurationSetName: StrictStr
