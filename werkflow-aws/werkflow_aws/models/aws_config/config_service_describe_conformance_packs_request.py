from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_describe_conformance_packs_filters import ConfigServiceDescribeConformancePacksFilters


class ConfigServiceDescribeConformancePacksRequest(BaseModel):
    ConformancePackNames: list[StrictStr] | None = None
    Filters: ConfigServiceDescribeConformancePacksFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
