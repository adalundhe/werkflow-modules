from __future__ import annotations
from pydantic import BaseModel
from .config_service_field_info import ConfigServiceFieldInfo


class ConfigServiceQueryInfo(BaseModel):
    SelectFields: list[ConfigServiceFieldInfo] | None = None
