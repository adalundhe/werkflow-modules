from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_contact_metric_value import ConnectContactMetricValue


class ConnectContactMetricResult(BaseModel):
    Name: StrictStr | None = None
    Value: ConnectContactMetricValue | None = None
