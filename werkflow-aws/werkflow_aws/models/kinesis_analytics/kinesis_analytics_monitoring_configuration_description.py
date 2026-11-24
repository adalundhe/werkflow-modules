from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsMonitoringConfigurationDescription(BaseModel):
    ConfigurationType: StrictStr | None = None
    MetricsLevel: StrictStr | None = None
    LogLevel: StrictStr | None = None
