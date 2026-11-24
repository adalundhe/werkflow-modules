from __future__ import annotations
from pydantic import BaseModel
from .config_service_config_rule import ConfigServiceConfigRule
from .config_service_tag import ConfigServiceTag


class ConfigServicePutConfigRuleRequest(BaseModel):
    ConfigRule: ConfigServiceConfigRule
    Tags: list[ConfigServiceTag] | None = None
