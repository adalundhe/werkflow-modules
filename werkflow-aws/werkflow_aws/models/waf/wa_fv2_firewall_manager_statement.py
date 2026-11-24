from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_managed_rule_group_statement import WAFv2ManagedRuleGroupStatement
from .wa_fv2_rule_group_reference_statement import WAFv2RuleGroupReferenceStatement


class WAFv2FirewallManagerStatement(BaseModel):
    ManagedRuleGroupStatement: WAFv2ManagedRuleGroupStatement | None = None
    RuleGroupReferenceStatement: WAFv2RuleGroupReferenceStatement | None = None
