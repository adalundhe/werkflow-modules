from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_security_control_definition import SecurityHubSecurityControlDefinition


class SecurityHubGetSecurityControlDefinitionResponse(BaseModel):
    SecurityControlDefinition: SecurityHubSecurityControlDefinition | None = None
    ResponseMetadata: dict[str, Any] | None = None
