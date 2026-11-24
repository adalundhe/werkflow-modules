from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_account_aggregation_source import ConfigServiceAccountAggregationSource
from .config_service_aggregator_filters import ConfigServiceAggregatorFilters
from .config_service_organization_aggregation_source import ConfigServiceOrganizationAggregationSource


class ConfigServiceConfigurationAggregator(BaseModel):
    ConfigurationAggregatorName: StrictStr | None = None
    ConfigurationAggregatorArn: StrictStr | None = None
    AccountAggregationSources: list[ConfigServiceAccountAggregationSource] | None = None
    OrganizationAggregationSource: ConfigServiceOrganizationAggregationSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    AggregatorFilters: ConfigServiceAggregatorFilters | None = None
