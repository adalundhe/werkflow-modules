from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_rule_group_source_list_details import SecurityHubRuleGroupSourceListDetails
from .security_hub_rule_group_source_stateful_rules_details import SecurityHubRuleGroupSourceStatefulRulesDetails
from .security_hub_rule_group_source_stateless_rules_and_custom_actions_details import SecurityHubRuleGroupSourceStatelessRulesAndCustomActionsDetails


class SecurityHubRuleGroupSource(BaseModel):
    RulesSourceList: SecurityHubRuleGroupSourceListDetails | None = None
    RulesString: StrictStr | None = None
    StatefulRules: list[SecurityHubRuleGroupSourceStatefulRulesDetails] | None = None
    StatelessRulesAndCustomActions: SecurityHubRuleGroupSourceStatelessRulesAndCustomActionsDetails | None = None
