from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_conformance_pack_compliance_filters import ConfigServiceConformancePackComplianceFilters


class ConfigServiceDescribeConformancePackComplianceRequest(BaseModel):
    ConformancePackName: StrictStr
    Filters: ConfigServiceConformancePackComplianceFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
