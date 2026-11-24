from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_remediation_guidance import SecurityHubRemediationGuidance
from .security_hub_remediation_outcome import SecurityHubRemediationOutcome
from .security_hub_remediation_resource import SecurityHubRemediationResource
from .security_hub_remediation_summary_detail import SecurityHubRemediationSummaryDetail
from .security_hub_remediation_trait import SecurityHubRemediationTrait


class SecurityHubRemediationV2Item(BaseModel):
    TargetUid: StrictStr | None = None
    Outcome: SecurityHubRemediationOutcome | None = None
    Priority: StrictStr | None = None
    RemediationSummary: SecurityHubRemediationSummaryDetail | None = None
    Resource: SecurityHubRemediationResource | None = None
    Status: StrictStr | None = None
    Trait: SecurityHubRemediationTrait | None = None
    Guidance: SecurityHubRemediationGuidance | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
