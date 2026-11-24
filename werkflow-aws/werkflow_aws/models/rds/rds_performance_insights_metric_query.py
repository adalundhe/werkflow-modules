from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_performance_insights_metric_dimension_group import RDSPerformanceInsightsMetricDimensionGroup


class RDSPerformanceInsightsMetricQuery(BaseModel):
    GroupBy: RDSPerformanceInsightsMetricDimensionGroup | None = None
    Metric: StrictStr | None = None
