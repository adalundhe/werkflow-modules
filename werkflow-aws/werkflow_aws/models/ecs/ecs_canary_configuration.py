from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ECSCanaryConfiguration(BaseModel):
    canaryPercent: StrictFloat | StrictInt | None = None
    canaryBakeTimeInMinutes: StrictInt | None = None
