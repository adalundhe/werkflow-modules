from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .security_hub_automation_rules_action_type_object_v2 import SecurityHubAutomationRulesActionTypeObjectV2


class SecurityHubAutomationRulesMetadataV2(BaseModel):
    RuleArn: StrictStr | None = None
    RuleId: StrictStr | None = None
    RuleOrder: StrictFloat | StrictInt | None = None
    RuleName: StrictStr | None = None
    RuleStatus: StrictStr | None = None
    Description: StrictStr | None = None
    Actions: list[SecurityHubAutomationRulesActionTypeObjectV2] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
