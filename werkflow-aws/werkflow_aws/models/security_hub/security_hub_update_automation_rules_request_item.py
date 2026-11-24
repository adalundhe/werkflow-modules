from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_automation_rules_action import SecurityHubAutomationRulesAction
from .security_hub_automation_rules_finding_filters import SecurityHubAutomationRulesFindingFilters


class SecurityHubUpdateAutomationRulesRequestItem(BaseModel):
    RuleArn: StrictStr
    RuleStatus: Literal['ENABLED', 'DISABLED'] | None = None
    RuleOrder: StrictInt | None = None
    Description: StrictStr | None = None
    RuleName: StrictStr | None = None
    IsTerminal: StrictBool | None = None
    Criteria: SecurityHubAutomationRulesFindingFilters | None = None
    Actions: list[SecurityHubAutomationRulesAction] | None = None
