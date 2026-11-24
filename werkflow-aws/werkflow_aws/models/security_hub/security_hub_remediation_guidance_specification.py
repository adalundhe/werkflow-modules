from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_remediation_parameter import SecurityHubRemediationParameter
from .security_hub_remediation_step import SecurityHubRemediationStep


class SecurityHubRemediationGuidanceSpecification(BaseModel):
    Parameters: list[SecurityHubRemediationParameter] | None = None
    Steps: list[SecurityHubRemediationStep] | None = None
    ExpectedEndState: StrictStr | None = None
    RequiredPermissions: list[StrictStr] | None = None
