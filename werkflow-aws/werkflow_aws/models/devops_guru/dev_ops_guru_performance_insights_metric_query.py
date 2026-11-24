from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_performance_insights_metric_dimension_group import DevOpsGuruPerformanceInsightsMetricDimensionGroup


class DevOpsGuruPerformanceInsightsMetricQuery(BaseModel):
    Metric: StrictStr | None = None
    GroupBy: DevOpsGuruPerformanceInsightsMetricDimensionGroup | None = None
    Filter: dict[StrictStr, StrictStr] | None = None
