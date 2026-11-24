from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetConfigurationSetRequest(BaseModel):
    ConfigurationSetName: StrictStr
