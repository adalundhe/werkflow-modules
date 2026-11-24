from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_rule_action import WAFv2RuleAction


class WAFv2RuleActionOverride(BaseModel):
    Name: StrictStr | None = None
    ActionToUse: WAFv2RuleAction | None = None
