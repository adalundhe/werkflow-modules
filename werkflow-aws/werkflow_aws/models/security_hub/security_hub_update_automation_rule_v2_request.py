from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_automation_rules_action_v2 import SecurityHubAutomationRulesActionV2
from .security_hub_criteria import SecurityHubCriteria


class SecurityHubUpdateAutomationRuleV2Request(BaseModel):
    Identifier: StrictStr
    RuleStatus: Literal['ENABLED', 'DISABLED'] | None = None
    RuleOrder: StrictFloat | StrictInt | None = None
    Description: StrictStr | None = None
    RuleName: StrictStr | None = None
    Criteria: SecurityHubCriteria | None = None
    Actions: list[SecurityHubAutomationRulesActionV2] | None = None
