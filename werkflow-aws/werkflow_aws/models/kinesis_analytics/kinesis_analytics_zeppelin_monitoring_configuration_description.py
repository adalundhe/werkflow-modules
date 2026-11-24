from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsZeppelinMonitoringConfigurationDescription(BaseModel):
    LogLevel: StrictStr | None = None
