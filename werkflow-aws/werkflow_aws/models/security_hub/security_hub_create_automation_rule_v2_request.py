from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_automation_rules_action_v2 import SecurityHubAutomationRulesActionV2
from .security_hub_criteria import SecurityHubCriteria


class SecurityHubCreateAutomationRuleV2Request(BaseModel):
    RuleName: StrictStr
    Description: StrictStr
    RuleOrder: StrictFloat | StrictInt
    Criteria: SecurityHubCriteria
    Actions: list[SecurityHubAutomationRulesActionV2]
    RuleStatus: Literal['ENABLED', 'DISABLED'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
