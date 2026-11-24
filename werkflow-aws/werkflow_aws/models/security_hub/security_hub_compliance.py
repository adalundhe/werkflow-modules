from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_associated_standard import SecurityHubAssociatedStandard
from .security_hub_security_control_parameter import SecurityHubSecurityControlParameter
from .security_hub_status_reason import SecurityHubStatusReason


class SecurityHubCompliance(BaseModel):
    Status: StrictStr | None = None
    RelatedRequirements: list[StrictStr] | None = None
    StatusReasons: list[SecurityHubStatusReason] | None = None
    SecurityControlId: StrictStr | None = None
    AssociatedStandards: list[SecurityHubAssociatedStandard] | None = None
    SecurityControlParameters: list[SecurityHubSecurityControlParameter] | None = None
