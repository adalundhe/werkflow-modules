from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_alert_target import IoTAlertTarget
from .io_t_behavior import IoTBehavior
from .io_t_metric_to_retain import IoTMetricToRetain
from .io_t_metrics_export_config import IoTMetricsExportConfig


class IoTUpdateSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    securityProfileDescription: StrictStr | None = None
    behaviors: list[IoTBehavior] | None = None
    alertTargets: dict[Literal['SNS'], IoTAlertTarget] | None = None
    additionalMetricsToRetain: list[StrictStr] | None = None
    additionalMetricsToRetainV2: list[IoTMetricToRetain] | None = None
    deleteBehaviors: StrictBool | None = None
    deleteAlertTargets: StrictBool | None = None
    deleteAdditionalMetricsToRetain: StrictBool | None = None
    expectedVersion: StrictInt | None = None
    metricsExportConfig: IoTMetricsExportConfig | None = None
    deleteMetricsExportConfig: StrictBool | None = None
