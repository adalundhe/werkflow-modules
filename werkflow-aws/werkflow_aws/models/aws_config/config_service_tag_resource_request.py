from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_tag import ConfigServiceTag


class ConfigServiceTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[ConfigServiceTag]
