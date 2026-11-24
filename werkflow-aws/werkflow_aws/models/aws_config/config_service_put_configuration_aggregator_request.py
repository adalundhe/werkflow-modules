from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_account_aggregation_source import ConfigServiceAccountAggregationSource
from .config_service_aggregator_filters import ConfigServiceAggregatorFilters
from .config_service_organization_aggregation_source import ConfigServiceOrganizationAggregationSource
from .config_service_tag import ConfigServiceTag


class ConfigServicePutConfigurationAggregatorRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    AccountAggregationSources: list[ConfigServiceAccountAggregationSource] | None = None
    OrganizationAggregationSource: ConfigServiceOrganizationAggregationSource | None = None
    Tags: list[ConfigServiceTag] | None = None
    AggregatorFilters: ConfigServiceAggregatorFilters | None = None
