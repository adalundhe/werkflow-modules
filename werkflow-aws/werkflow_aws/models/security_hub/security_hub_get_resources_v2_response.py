from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_resource_result import SecurityHubResourceResult


class SecurityHubGetResourcesV2Response(BaseModel):
    Resources: list[SecurityHubResourceResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
