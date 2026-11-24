from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ECSLinearConfiguration(BaseModel):
    stepPercent: StrictFloat | StrictInt | None = None
    stepBakeTimeInMinutes: StrictInt | None = None
