from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_automation_rules_finding_fields_update import SecurityHubAutomationRulesFindingFieldsUpdate


class SecurityHubAutomationRulesAction(BaseModel):
    Type: StrictStr | None = None
    FindingFieldsUpdate: SecurityHubAutomationRulesFindingFieldsUpdate | None = None
