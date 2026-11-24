from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class IoTMetricValue(BaseModel):
    count: StrictInt | None = None
    cidrs: list[StrictStr] | None = None
    ports: list[StrictInt] | None = None
    number: StrictFloat | StrictInt | None = None
    numbers: list[StrictFloat | StrictInt] | None = None
    strings: list[StrictStr] | None = None
