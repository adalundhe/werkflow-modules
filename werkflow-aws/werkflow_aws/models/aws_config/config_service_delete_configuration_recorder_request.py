from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteConfigurationRecorderRequest(BaseModel):
    ConfigurationRecorderName: StrictStr
