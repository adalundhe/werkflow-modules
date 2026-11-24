from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceStartConfigurationRecorderRequest(BaseModel):
    ConfigurationRecorderName: StrictStr
