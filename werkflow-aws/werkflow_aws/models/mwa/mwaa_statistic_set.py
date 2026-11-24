from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class MWAAStatisticSet(BaseModel):
    SampleCount: StrictInt | None = None
    Sum: StrictFloat | StrictInt | None = None
    Minimum: StrictFloat | StrictInt | None = None
    Maximum: StrictFloat | StrictInt | None = None
