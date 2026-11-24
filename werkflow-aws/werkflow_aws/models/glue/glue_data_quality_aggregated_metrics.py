from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueDataQualityAggregatedMetrics(BaseModel):
    TotalRowsProcessed: StrictFloat | StrictInt | None = None
    TotalRowsPassed: StrictFloat | StrictInt | None = None
    TotalRowsFailed: StrictFloat | StrictInt | None = None
    TotalRulesProcessed: StrictFloat | StrictInt | None = None
    TotalRulesPassed: StrictFloat | StrictInt | None = None
    TotalRulesFailed: StrictFloat | StrictInt | None = None
