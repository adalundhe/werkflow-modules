from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_watch_logs_metric_transformation import CloudWatchLogsMetricTransformation


class CloudWatchLogsPutMetricFilterRequest(BaseModel):
    logGroupName: StrictStr
    filterName: StrictStr
    filterPattern: StrictStr
    metricTransformations: list[CloudWatchLogsMetricTransformation]
    applyOnTransformedLogs: StrictBool | None = None
    fieldSelectionCriteria: StrictStr | None = None
    emitSystemFieldDimensions: list[StrictStr] | None = None
