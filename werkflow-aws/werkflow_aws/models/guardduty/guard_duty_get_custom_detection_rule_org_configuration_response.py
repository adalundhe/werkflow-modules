from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_detection_rule_org_configuration import GuardDutyDetectionRuleOrgConfiguration


class GuardDutyGetCustomDetectionRuleOrgConfigurationResponse(BaseModel):
    Configuration: GuardDutyDetectionRuleOrgConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
