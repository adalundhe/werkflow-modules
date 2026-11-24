from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_conformance_pack_compliance_summary import ConfigServiceAggregateConformancePackComplianceSummary


class ConfigServiceGetAggregateConformancePackComplianceSummaryResponse(BaseModel):
    AggregateConformancePackComplianceSummaries: list[ConfigServiceAggregateConformancePackComplianceSummary] | None = None
    GroupByKey: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
