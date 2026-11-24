from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_cloud_watch_metrics_detail import DevOpsGuruCloudWatchMetricsDetail
from .dev_ops_guru_performance_insights_metrics_detail import DevOpsGuruPerformanceInsightsMetricsDetail


class DevOpsGuruAnomalySourceDetails(BaseModel):
    CloudWatchMetrics: list[DevOpsGuruCloudWatchMetricsDetail] | None = None
    PerformanceInsightsMetrics: list[DevOpsGuruPerformanceInsightsMetricsDetail] | None = None
