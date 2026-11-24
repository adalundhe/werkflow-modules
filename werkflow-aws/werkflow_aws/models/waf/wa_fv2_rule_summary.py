from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_rule_action import WAFv2RuleAction


class WAFv2RuleSummary(BaseModel):
    Name: StrictStr | None = None
    Action: WAFv2RuleAction | None = None
