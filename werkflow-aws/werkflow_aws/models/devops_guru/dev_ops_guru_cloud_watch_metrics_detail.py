from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_cloud_watch_metrics_data_summary import DevOpsGuruCloudWatchMetricsDataSummary
from .dev_ops_guru_cloud_watch_metrics_dimension import DevOpsGuruCloudWatchMetricsDimension


class DevOpsGuruCloudWatchMetricsDetail(BaseModel):
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Dimensions: list[DevOpsGuruCloudWatchMetricsDimension] | None = None
    Stat: StrictStr | None = None
    Unit: StrictStr | None = None
    Period: StrictInt | None = None
    MetricDataSummary: DevOpsGuruCloudWatchMetricsDataSummary | None = None
