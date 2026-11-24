from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_timestamp_metric_value_pair import DevOpsGuruTimestampMetricValuePair


class DevOpsGuruCloudWatchMetricsDataSummary(BaseModel):
    TimestampMetricValuePairList: list[DevOpsGuruTimestampMetricValuePair] | None = None
    StatusCode: StrictStr | None = None
