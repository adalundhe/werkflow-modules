from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightAxisLinearScale(BaseModel):
    StepCount: StrictInt | None = None
    StepSize: StrictFloat | StrictInt | None = None
