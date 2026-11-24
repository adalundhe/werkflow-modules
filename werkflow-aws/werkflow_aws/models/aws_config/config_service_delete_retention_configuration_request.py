from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteRetentionConfigurationRequest(BaseModel):
    RetentionConfigurationName: StrictStr
