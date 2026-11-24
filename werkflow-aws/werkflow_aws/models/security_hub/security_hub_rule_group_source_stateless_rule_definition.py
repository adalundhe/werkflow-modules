from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_rule_group_source_stateless_rule_match_attributes import SecurityHubRuleGroupSourceStatelessRuleMatchAttributes


class SecurityHubRuleGroupSourceStatelessRuleDefinition(BaseModel):
    Actions: list[StrictStr] | None = None
    MatchAttributes: SecurityHubRuleGroupSourceStatelessRuleMatchAttributes | None = None
