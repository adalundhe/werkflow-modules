from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_security_control_custom_parameter import SecurityHubSecurityControlCustomParameter


class SecurityHubSecurityControlsConfiguration(BaseModel):
    EnabledSecurityControlIdentifiers: list[StrictStr] | None = None
    DisabledSecurityControlIdentifiers: list[StrictStr] | None = None
    SecurityControlCustomParameters: list[SecurityHubSecurityControlCustomParameter] | None = None
