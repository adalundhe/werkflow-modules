from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_rule_group_source_stateful_rules_header_details import SecurityHubRuleGroupSourceStatefulRulesHeaderDetails
from .security_hub_rule_group_source_stateful_rules_options_details import SecurityHubRuleGroupSourceStatefulRulesOptionsDetails


class SecurityHubRuleGroupSourceStatefulRulesDetails(BaseModel):
    Action: StrictStr | None = None
    Header: SecurityHubRuleGroupSourceStatefulRulesHeaderDetails | None = None
    RuleOptions: list[SecurityHubRuleGroupSourceStatefulRulesOptionsDetails] | None = None
