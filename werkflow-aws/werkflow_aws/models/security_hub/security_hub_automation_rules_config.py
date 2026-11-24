from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_automation_rules_action import SecurityHubAutomationRulesAction
from .security_hub_automation_rules_finding_filters import SecurityHubAutomationRulesFindingFilters


class SecurityHubAutomationRulesConfig(BaseModel):
    RuleArn: StrictStr | None = None
    RuleStatus: StrictStr | None = None
    RuleOrder: StrictInt | None = None
    RuleName: StrictStr | None = None
    Description: StrictStr | None = None
    IsTerminal: StrictBool | None = None
    Criteria: SecurityHubAutomationRulesFindingFilters | None = None
    Actions: list[SecurityHubAutomationRulesAction] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
