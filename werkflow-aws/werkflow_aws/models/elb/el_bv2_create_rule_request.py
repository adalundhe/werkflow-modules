from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .el_bv2_action import ELBv2Action
from .el_bv2_rule_condition import ELBv2RuleCondition
from .el_bv2_rule_transform import ELBv2RuleTransform
from .el_bv2_tag import ELBv2Tag


class ELBv2CreateRuleRequest(BaseModel):
    ListenerArn: StrictStr
    Conditions: list[ELBv2RuleCondition]
    Priority: StrictInt
    Actions: list[ELBv2Action]
    Tags: list[ELBv2Tag] | None = None
    Transforms: list[ELBv2RuleTransform] | None = None
