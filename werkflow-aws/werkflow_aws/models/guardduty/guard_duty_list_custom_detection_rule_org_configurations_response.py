from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_detection_rule_org_configuration_summary import GuardDutyDetectionRuleOrgConfigurationSummary


class GuardDutyListCustomDetectionRuleOrgConfigurationsResponse(BaseModel):
    Configurations: list[GuardDutyDetectionRuleOrgConfigurationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
