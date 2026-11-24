from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr
from .wa_fv2_excluded_rule import WAFv2ExcludedRule
from .wa_fv2_managed_rule_group_config import WAFv2ManagedRuleGroupConfig
from .wa_fv2_rule_action_override import WAFv2RuleActionOverride

if TYPE_CHECKING:
    from .wa_fv2_statement import WAFv2Statement


class WAFv2ManagedRuleGroupStatement(BaseModel):
    VendorName: StrictStr | None = None
    Name: StrictStr | None = None
    Version: StrictStr | None = None
    ExcludedRules: list[WAFv2ExcludedRule] | None = None
    ScopeDownStatement: WAFv2Statement | None = None
    ManagedRuleGroupConfigs: list[WAFv2ManagedRuleGroupConfig] | None = None
    RuleActionOverrides: list[WAFv2RuleActionOverride] | None = None
