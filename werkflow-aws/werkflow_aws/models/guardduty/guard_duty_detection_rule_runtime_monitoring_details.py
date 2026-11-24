from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_detection_rule_runtime_platforms import GuardDutyDetectionRuleRuntimePlatforms


class GuardDutyDetectionRuleRuntimeMonitoringDetails(BaseModel):
    Platforms: GuardDutyDetectionRuleRuntimePlatforms | None = None
