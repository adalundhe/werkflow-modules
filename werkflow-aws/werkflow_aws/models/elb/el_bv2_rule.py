from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .el_bv2_action import ELBv2Action
from .el_bv2_rule_condition import ELBv2RuleCondition
from .el_bv2_rule_transform import ELBv2RuleTransform


class ELBv2Rule(BaseModel):
    RuleArn: StrictStr | None = None
    Priority: StrictStr | None = None
    Conditions: list[ELBv2RuleCondition] | None = None
    Actions: list[ELBv2Action] | None = None
    IsDefault: StrictBool | None = None
    Transforms: list[ELBv2RuleTransform] | None = None
