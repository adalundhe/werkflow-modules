from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_compliance_by_conformance_pack import ConfigServiceAggregateComplianceByConformancePack


class ConfigServiceDescribeAggregateComplianceByConformancePacksResponse(BaseModel):
    AggregateComplianceByConformancePacks: list[ConfigServiceAggregateComplianceByConformancePack] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
