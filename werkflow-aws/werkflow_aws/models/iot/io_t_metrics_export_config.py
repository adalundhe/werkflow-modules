from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTMetricsExportConfig(BaseModel):
    mqttTopic: StrictStr | None = None
    roleArn: StrictStr | None = None
