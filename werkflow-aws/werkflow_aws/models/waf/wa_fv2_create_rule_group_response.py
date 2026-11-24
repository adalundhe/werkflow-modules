from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_rule_group_summary import WAFv2RuleGroupSummary


class WAFv2CreateRuleGroupResponse(BaseModel):
    Summary: WAFv2RuleGroupSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
