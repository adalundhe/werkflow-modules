from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_pre_evaluation_filters import ConnectPreEvaluationFilters
from .connect_rule_action import ConnectRuleAction
from .connect_rule_trigger_event_source import ConnectRuleTriggerEventSource


class ConnectCreateRuleRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    TriggerEventSource: ConnectRuleTriggerEventSource
    Function: StrictStr
    Actions: list[ConnectRuleAction]
    PublishStatus: Literal['DRAFT', 'PUBLISHED']
    PreEvaluationFilters: ConnectPreEvaluationFilters | None = None
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
