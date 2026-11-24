from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_note_update import SecurityHubNoteUpdate
from .security_hub_related_finding import SecurityHubRelatedFinding
from .security_hub_severity_update import SecurityHubSeverityUpdate
from .security_hub_workflow_update import SecurityHubWorkflowUpdate


class SecurityHubAutomationRulesFindingFieldsUpdate(BaseModel):
    Note: SecurityHubNoteUpdate | None = None
    Severity: SecurityHubSeverityUpdate | None = None
    VerificationState: StrictStr | None = None
    Confidence: StrictInt | None = None
    Criticality: StrictInt | None = None
    Types: list[StrictStr] | None = None
    UserDefinedFields: dict[StrictStr, StrictStr] | None = None
    Workflow: SecurityHubWorkflowUpdate | None = None
    RelatedFindings: list[SecurityHubRelatedFinding] | None = None
