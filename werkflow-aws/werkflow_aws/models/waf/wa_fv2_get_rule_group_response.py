from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_rule_group import WAFv2RuleGroup


class WAFv2GetRuleGroupResponse(BaseModel):
    RuleGroup: WAFv2RuleGroup | None = None
    LockToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
