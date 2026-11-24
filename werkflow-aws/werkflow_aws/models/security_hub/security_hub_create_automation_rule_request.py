from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_automation_rules_action import SecurityHubAutomationRulesAction
from .security_hub_automation_rules_finding_filters import SecurityHubAutomationRulesFindingFilters


class SecurityHubCreateAutomationRuleRequest(BaseModel):
    RuleOrder: StrictInt
    RuleName: StrictStr
    Description: StrictStr
    Criteria: SecurityHubAutomationRulesFindingFilters
    Actions: list[SecurityHubAutomationRulesAction]
    Tags: dict[StrictStr, StrictStr] | None = None
    RuleStatus: Literal['ENABLED', 'DISABLED'] | None = None
    IsTerminal: StrictBool | None = None
