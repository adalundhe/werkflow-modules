from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_aggregate_conformance_pack_compliance_summary_filters import ConfigServiceAggregateConformancePackComplianceSummaryFilters


class ConfigServiceGetAggregateConformancePackComplianceSummaryRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    Filters: ConfigServiceAggregateConformancePackComplianceSummaryFilters | None = None
    GroupByKey: Literal['ACCOUNT_ID', 'AWS_REGION'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
