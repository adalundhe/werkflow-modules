from __future__ import annotations
from pydantic import BaseModel
from .rds_performance_insights_metric_query import RDSPerformanceInsightsMetricQuery


class RDSMetricQuery(BaseModel):
    PerformanceInsightsMetricQuery: RDSPerformanceInsightsMetricQuery | None = None
