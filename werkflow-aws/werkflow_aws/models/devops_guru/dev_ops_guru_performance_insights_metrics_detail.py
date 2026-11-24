from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_performance_insights_metric_query import DevOpsGuruPerformanceInsightsMetricQuery
from .dev_ops_guru_performance_insights_reference_data import DevOpsGuruPerformanceInsightsReferenceData
from .dev_ops_guru_performance_insights_stat import DevOpsGuruPerformanceInsightsStat


class DevOpsGuruPerformanceInsightsMetricsDetail(BaseModel):
    MetricDisplayName: StrictStr | None = None
    Unit: StrictStr | None = None
    MetricQuery: DevOpsGuruPerformanceInsightsMetricQuery | None = None
    ReferenceData: list[DevOpsGuruPerformanceInsightsReferenceData] | None = None
    StatsAtAnomaly: list[DevOpsGuruPerformanceInsightsStat] | None = None
    StatsAtBaseline: list[DevOpsGuruPerformanceInsightsStat] | None = None
