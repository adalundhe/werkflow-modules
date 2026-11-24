from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_dimension_model import CloudWatchDimensionModel
from .cloud_watch_metric_math_anomaly_detector import CloudWatchMetricMathAnomalyDetector
from .cloud_watch_single_metric_anomaly_detector import CloudWatchSingleMetricAnomalyDetector


class CloudWatchDeleteAnomalyDetectorRequest(BaseModel):
    AnomalyDetectorId: StrictStr | None = None
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    Stat: StrictStr | None = None
    SingleMetricAnomalyDetector: CloudWatchSingleMetricAnomalyDetector | None = None
    MetricMathAnomalyDetector: CloudWatchMetricMathAnomalyDetector | None = None
