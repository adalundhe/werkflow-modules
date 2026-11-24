from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_automation_rules_action_v2 import SecurityHubAutomationRulesActionV2
from .security_hub_criteria import SecurityHubCriteria


class SecurityHubGetAutomationRuleV2Response(BaseModel):
    RuleArn: StrictStr | None = None
    RuleId: StrictStr | None = None
    RuleOrder: StrictFloat | StrictInt | None = None
    RuleName: StrictStr | None = None
    RuleStatus: StrictStr | None = None
    Description: StrictStr | None = None
    Criteria: SecurityHubCriteria | None = None
    Actions: list[SecurityHubAutomationRulesActionV2] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
