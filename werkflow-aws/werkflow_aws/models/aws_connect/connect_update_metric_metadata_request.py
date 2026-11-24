from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateMetricMetadataRequest(BaseModel):
    InstanceId: StrictStr
    MetricId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
