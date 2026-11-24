from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDeleteConfigurationRequest(BaseModel):
    ConfigurationId: StrictStr
