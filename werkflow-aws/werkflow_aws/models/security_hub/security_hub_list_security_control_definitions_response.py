from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_security_control_definition import SecurityHubSecurityControlDefinition


class SecurityHubListSecurityControlDefinitionsResponse(BaseModel):
    SecurityControlDefinitions: list[SecurityHubSecurityControlDefinition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
