from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_alert_target import IoTAlertTarget
from .io_t_behavior import IoTBehavior
from .io_t_metric_to_retain import IoTMetricToRetain
from .io_t_metrics_export_config import IoTMetricsExportConfig


class IoTUpdateSecurityProfileResponse(BaseModel):
    securityProfileName: StrictStr | None = None
    securityProfileArn: StrictStr | None = None
    securityProfileDescription: StrictStr | None = None
    behaviors: list[IoTBehavior] | None = None
    alertTargets: dict[StrictStr, IoTAlertTarget] | None = None
    additionalMetricsToRetain: list[StrictStr] | None = None
    additionalMetricsToRetainV2: list[IoTMetricToRetain] | None = None
    version: StrictInt | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    metricsExportConfig: IoTMetricsExportConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
