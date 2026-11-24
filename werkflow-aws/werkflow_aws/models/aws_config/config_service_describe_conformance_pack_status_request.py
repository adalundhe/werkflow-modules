from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_describe_conformance_packs_filters import ConfigServiceDescribeConformancePacksFilters


class ConfigServiceDescribeConformancePackStatusRequest(BaseModel):
    ConformancePackNames: list[StrictStr] | None = None
    Filters: ConfigServiceDescribeConformancePacksFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
