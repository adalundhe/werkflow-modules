from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteConfigurationAggregatorRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
