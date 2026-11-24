from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCloudwatchMetricAction(BaseModel):
    roleArn: StrictStr | None = None
    metricNamespace: StrictStr | None = None
    metricName: StrictStr | None = None
    metricValue: StrictStr | None = None
    metricUnit: StrictStr | None = None
    metricTimestamp: StrictStr | None = None
