from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_tag import ConfigServiceTag


class ConfigServicePutServiceLinkedConfigurationRecorderRequest(BaseModel):
    ServicePrincipal: StrictStr
    Tags: list[ConfigServiceTag] | None = None
