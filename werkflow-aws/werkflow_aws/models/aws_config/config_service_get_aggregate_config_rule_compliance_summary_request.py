from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_config_rule_compliance_summary_filters import ConfigServiceConfigRuleComplianceSummaryFilters


class ConfigServiceGetAggregateConfigRuleComplianceSummaryRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    Filters: ConfigServiceConfigRuleComplianceSummaryFilters | None = None
    GroupByKey: Literal['ACCOUNT_ID', 'AWS_REGION'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
