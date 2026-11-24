from __future__ import annotations
from pydantic import BaseModel
from .security_hub_rule_group_variables_ip_sets_details import SecurityHubRuleGroupVariablesIpSetsDetails
from .security_hub_rule_group_variables_port_sets_details import SecurityHubRuleGroupVariablesPortSetsDetails


class SecurityHubRuleGroupVariables(BaseModel):
    IpSets: SecurityHubRuleGroupVariablesIpSetsDetails | None = None
    PortSets: SecurityHubRuleGroupVariablesPortSetsDetails | None = None
