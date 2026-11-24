from __future__ import annotations
from pydantic import BaseModel
from .security_hub_rule_group_source import SecurityHubRuleGroupSource
from .security_hub_rule_group_variables import SecurityHubRuleGroupVariables


class SecurityHubRuleGroupDetails(BaseModel):
    RuleVariables: SecurityHubRuleGroupVariables | None = None
    RulesSource: SecurityHubRuleGroupSource | None = None
