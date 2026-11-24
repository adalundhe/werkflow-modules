from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_logs_metric_transformation import CloudWatchLogsMetricTransformation


class CloudWatchLogsMetricFilter(BaseModel):
    filterName: StrictStr | None = None
    filterPattern: StrictStr | None = None
    metricTransformations: list[CloudWatchLogsMetricTransformation] | None = None
    creationTime: StrictInt | None = None
    logGroupName: StrictStr | None = None
    applyOnTransformedLogs: StrictBool | None = None
    fieldSelectionCriteria: StrictStr | None = None
    emitSystemFieldDimensions: list[StrictStr] | None = None
