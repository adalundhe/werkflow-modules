from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_remediation_guidance_context import SecurityHubRemediationGuidanceContext
from .security_hub_remediation_guidance_examples import SecurityHubRemediationGuidanceExamples
from .security_hub_remediation_guidance_metadata import SecurityHubRemediationGuidanceMetadata
from .security_hub_remediation_guidance_specification import SecurityHubRemediationGuidanceSpecification


class SecurityHubRemediationGuidance(BaseModel):
    TargetTypeName: StrictStr | None = None
    Pattern: StrictStr | None = None
    Version: StrictStr | None = None
    Context: SecurityHubRemediationGuidanceContext | None = None
    Specification: SecurityHubRemediationGuidanceSpecification | None = None
    Examples: SecurityHubRemediationGuidanceExamples | None = None
    Metadata: SecurityHubRemediationGuidanceMetadata | None = None
