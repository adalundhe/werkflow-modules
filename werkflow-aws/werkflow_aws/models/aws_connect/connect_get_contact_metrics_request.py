from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_contact_metric_info import ConnectContactMetricInfo


class ConnectGetContactMetricsRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    Metrics: list[ConnectContactMetricInfo]
