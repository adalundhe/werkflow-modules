from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_security_controls_configuration import SecurityHubSecurityControlsConfiguration


class SecurityHubPolicyModel(BaseModel):
    ServiceEnabled: StrictBool | None = None
    EnabledStandardIdentifiers: list[StrictStr] | None = None
    SecurityControlsConfiguration: SecurityHubSecurityControlsConfiguration | None = None
