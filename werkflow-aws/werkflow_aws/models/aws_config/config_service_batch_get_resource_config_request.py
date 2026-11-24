from __future__ import annotations
from pydantic import BaseModel
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceBatchGetResourceConfigRequest(BaseModel):
    resourceKeys: list[ConfigServiceResourceKey]
