from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2DataQuery(BaseModel):
    Id: StrictStr | None = None
    Source: StrictStr | None = None
    Destination: StrictStr | None = None
    Metric: Literal['aggregate-latency'] | None = None
    Statistic: Literal['p50'] | None = None
    Period: Literal['five-minutes', 'fifteen-minutes', 'one-hour', 'three-hours', 'one-day', 'one-week'] | None = None
