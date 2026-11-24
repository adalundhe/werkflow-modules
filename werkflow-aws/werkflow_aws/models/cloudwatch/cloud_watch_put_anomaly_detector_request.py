from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_anomaly_detector_configuration import CloudWatchAnomalyDetectorConfiguration
from .cloud_watch_dimension_model import CloudWatchDimensionModel
from .cloud_watch_metric_characteristics import CloudWatchMetricCharacteristics
from .cloud_watch_metric_math_anomaly_detector import CloudWatchMetricMathAnomalyDetector
from .cloud_watch_single_metric_anomaly_detector import CloudWatchSingleMetricAnomalyDetector


class CloudWatchPutAnomalyDetectorRequest(BaseModel):
    Namespace: StrictStr | None = None
    MetricName: StrictStr | None = None
    Dimensions: list[CloudWatchDimensionModel] | None = None
    Stat: StrictStr | None = None
    Configuration: CloudWatchAnomalyDetectorConfiguration | None = None
    MetricCharacteristics: CloudWatchMetricCharacteristics | None = None
    SingleMetricAnomalyDetector: CloudWatchSingleMetricAnomalyDetector | None = None
    MetricMathAnomalyDetector: CloudWatchMetricMathAnomalyDetector | None = None
