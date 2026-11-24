from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectMetricFilterV2(BaseModel):
    MetricFilterKey: StrictStr | None = None
    MetricFilterValues: list[StrictStr] | None = None
    Negate: StrictBool | None = None
