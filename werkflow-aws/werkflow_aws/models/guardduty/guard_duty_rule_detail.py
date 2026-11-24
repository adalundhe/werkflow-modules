from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_detection_rule_runtime_monitoring_details import GuardDutyDetectionRuleRuntimeMonitoringDetails
from .guard_duty_rule_definition import GuardDutyRuleDefinition


class GuardDutyRuleDetail(BaseModel):
    RuleId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Severity: StrictStr | None = None
    DataSource: StrictStr | None = None
    Tactic: StrictStr | None = None
    Technique: StrictStr | None = None
    Service: StrictStr | None = None
    Definition: GuardDutyRuleDefinition | None = None
    Language: StrictStr | None = None
    Schema: StrictStr | None = None
    RuntimeMonitoringDetails: GuardDutyDetectionRuleRuntimeMonitoringDetails | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
