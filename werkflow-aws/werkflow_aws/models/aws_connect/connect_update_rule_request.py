from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_pre_evaluation_filters import ConnectPreEvaluationFilters
from .connect_rule_action import ConnectRuleAction


class ConnectUpdateRuleRequest(BaseModel):
    RuleId: StrictStr
    InstanceId: StrictStr
    Name: StrictStr
    Function: StrictStr
    Actions: list[ConnectRuleAction]
    PublishStatus: Literal['DRAFT', 'PUBLISHED']
    PreEvaluationFilters: ConnectPreEvaluationFilters | None = None
