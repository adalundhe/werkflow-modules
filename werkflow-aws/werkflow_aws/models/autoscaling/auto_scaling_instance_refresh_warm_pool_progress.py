from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AutoScalingInstanceRefreshWarmPoolProgress(BaseModel):
    PercentageComplete: StrictInt | None = None
    InstancesToUpdate: StrictInt | None = None
