from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCurrentMetric(BaseModel):
    Name: StrictStr | None = None
    MetricId: StrictStr | None = None
    Unit: StrictStr | None = None
