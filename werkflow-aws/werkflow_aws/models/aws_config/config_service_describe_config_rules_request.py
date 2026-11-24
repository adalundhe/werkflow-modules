from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_describe_config_rules_filters import ConfigServiceDescribeConfigRulesFilters


class ConfigServiceDescribeConfigRulesRequest(BaseModel):
    ConfigRuleNames: list[StrictStr] | None = None
    Filters: ConfigServiceDescribeConfigRulesFilters | None = None
    NextToken: StrictStr | None = None
