from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .security_hub_rule_group_source_stateless_rule_definition import SecurityHubRuleGroupSourceStatelessRuleDefinition


class SecurityHubRuleGroupSourceStatelessRulesDetails(BaseModel):
    Priority: StrictInt | None = None
    RuleDefinition: SecurityHubRuleGroupSourceStatelessRuleDefinition | None = None
