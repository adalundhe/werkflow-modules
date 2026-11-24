from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .el_bv2_action import ELBv2Action
from .el_bv2_rule_condition import ELBv2RuleCondition
from .el_bv2_rule_transform import ELBv2RuleTransform


class ELBv2ModifyRuleRequest(BaseModel):
    RuleArn: StrictStr
    Conditions: list[ELBv2RuleCondition] | None = None
    Actions: list[ELBv2Action] | None = None
    Transforms: list[ELBv2RuleTransform] | None = None
    ResetTransforms: StrictBool | None = None
