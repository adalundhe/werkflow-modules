from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_aggregate_conformance_pack_compliance_filters import ConfigServiceAggregateConformancePackComplianceFilters


class ConfigServiceDescribeAggregateComplianceByConformancePacksRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    Filters: ConfigServiceAggregateConformancePackComplianceFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
