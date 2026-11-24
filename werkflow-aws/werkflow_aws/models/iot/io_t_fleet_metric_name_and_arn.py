from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTFleetMetricNameAndArn(BaseModel):
    metricName: StrictStr | None = None
    metricArn: StrictStr | None = None
