from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceStartRemediationExecutionResponse(BaseModel):
    FailureMessage: StrictStr | None = None
    FailedItems: list[ConfigServiceResourceKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
