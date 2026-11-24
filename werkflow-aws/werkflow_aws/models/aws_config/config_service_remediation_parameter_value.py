from __future__ import annotations
from pydantic import BaseModel
from .config_service_resource_value import ConfigServiceResourceValue
from .config_service_static_value import ConfigServiceStaticValue


class ConfigServiceRemediationParameterValue(BaseModel):
    ResourceValue: ConfigServiceResourceValue | None = None
    StaticValue: ConfigServiceStaticValue | None = None
