from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_software_resource_result import SecurityHubSoftwareResourceResult


class SecurityHubGetSoftwareResourcesV2Response(BaseModel):
    SoftwareResources: list[SecurityHubSoftwareResourceResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
