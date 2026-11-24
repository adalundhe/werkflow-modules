from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_machine_learning_detection_config import IoTMachineLearningDetectionConfig
from .io_t_metric_value import IoTMetricValue
from .io_t_statistical_threshold import IoTStatisticalThreshold


class IoTBehaviorCriteria(BaseModel):
    comparisonOperator: StrictStr | None = None
    value: IoTMetricValue | None = None
    durationSeconds: StrictInt | None = None
    consecutiveDatapointsToAlarm: StrictInt | None = None
    consecutiveDatapointsToClear: StrictInt | None = None
    statisticalThreshold: IoTStatisticalThreshold | None = None
    mlDetectionConfig: IoTMachineLearningDetectionConfig | None = None
