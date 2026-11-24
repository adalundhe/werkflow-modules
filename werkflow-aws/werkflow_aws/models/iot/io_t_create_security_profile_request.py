from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_alert_target import IoTAlertTarget
from .io_t_behavior import IoTBehavior
from .io_t_metric_to_retain import IoTMetricToRetain
from .io_t_metrics_export_config import IoTMetricsExportConfig
from .io_t_tag import IoTTag


class IoTCreateSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    securityProfileDescription: StrictStr | None = None
    behaviors: list[IoTBehavior] | None = None
    alertTargets: dict[Literal['SNS'], IoTAlertTarget] | None = None
    additionalMetricsToRetain: list[StrictStr] | None = None
    additionalMetricsToRetainV2: list[IoTMetricToRetain] | None = None
    tags: list[IoTTag] | None = None
    metricsExportConfig: IoTMetricsExportConfig | None = None
