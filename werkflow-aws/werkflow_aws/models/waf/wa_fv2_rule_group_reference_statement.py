from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_excluded_rule import WAFv2ExcludedRule
from .wa_fv2_rule_action_override import WAFv2RuleActionOverride


class WAFv2RuleGroupReferenceStatement(BaseModel):
    ARN: StrictStr | None = None
    ExcludedRules: list[WAFv2ExcludedRule] | None = None
    RuleActionOverrides: list[WAFv2RuleActionOverride] | None = None
