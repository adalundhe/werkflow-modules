from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class IoTPercentPair(BaseModel):
    percent: StrictFloat | StrictInt | None = None
    value: StrictFloat | StrictInt | None = None
