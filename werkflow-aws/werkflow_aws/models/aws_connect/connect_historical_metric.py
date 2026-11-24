from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_threshold import ConnectThreshold


class ConnectHistoricalMetric(BaseModel):
    Name: StrictStr | None = None
    Threshold: ConnectThreshold | None = None
    Statistic: StrictStr | None = None
    Unit: StrictStr | None = None
