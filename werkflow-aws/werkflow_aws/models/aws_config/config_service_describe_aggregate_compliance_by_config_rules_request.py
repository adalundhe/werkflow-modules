from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_config_rule_compliance_filters import ConfigServiceConfigRuleComplianceFilters


class ConfigServiceDescribeAggregateComplianceByConfigRulesRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    Filters: ConfigServiceConfigRuleComplianceFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
