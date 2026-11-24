from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_performance_insights_metric_query import DevOpsGuruPerformanceInsightsMetricQuery


class DevOpsGuruPerformanceInsightsReferenceMetric(BaseModel):
    MetricQuery: DevOpsGuruPerformanceInsightsMetricQuery | None = None
