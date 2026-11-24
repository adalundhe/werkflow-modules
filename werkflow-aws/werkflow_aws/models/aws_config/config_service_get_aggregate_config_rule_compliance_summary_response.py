from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_compliance_count import ConfigServiceAggregateComplianceCount


class ConfigServiceGetAggregateConfigRuleComplianceSummaryResponse(BaseModel):
    GroupByKey: StrictStr | None = None
    AggregateComplianceCounts: list[ConfigServiceAggregateComplianceCount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
