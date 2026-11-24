from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2Subscription(BaseModel):
    Source: StrictStr | None = None
    Destination: StrictStr | None = None
    Metric: StrictStr | None = None
    Statistic: StrictStr | None = None
    Period: StrictStr | None = None
