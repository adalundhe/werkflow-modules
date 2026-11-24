from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_software_result import SecurityHubSoftwareResult


class SecurityHubGetSoftwareV2Response(BaseModel):
    Software: list[SecurityHubSoftwareResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
