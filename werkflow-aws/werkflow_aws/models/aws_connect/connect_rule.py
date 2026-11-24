from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_pre_evaluation_filters import ConnectPreEvaluationFilters
from .connect_rule_action import ConnectRuleAction
from .connect_rule_trigger_event_source import ConnectRuleTriggerEventSource


class ConnectRule(BaseModel):
    Name: StrictStr | None = None
    RuleId: StrictStr | None = None
    RuleArn: StrictStr | None = None
    TriggerEventSource: ConnectRuleTriggerEventSource | None = None
    RuleCapabilityTiers: list[StrictStr] | None = None
    Function: StrictStr | None = None
    Actions: list[ConnectRuleAction] | None = None
    PublishStatus: StrictStr | None = None
    PreEvaluationFilters: ConnectPreEvaluationFilters | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
