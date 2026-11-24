from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConfigServicePutRetentionConfigurationRequest(BaseModel):
    RetentionPeriodInDays: StrictInt
