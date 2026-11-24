from __future__ import annotations
from pydantic import BaseModel
from .config_service_ssm_controls import ConfigServiceSsmControls


class ConfigServiceExecutionControls(BaseModel):
    SsmControls: ConfigServiceSsmControls | None = None
