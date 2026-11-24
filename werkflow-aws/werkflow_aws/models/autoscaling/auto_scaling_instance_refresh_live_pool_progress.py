from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AutoScalingInstanceRefreshLivePoolProgress(BaseModel):
    PercentageComplete: StrictInt | None = None
    InstancesToUpdate: StrictInt | None = None
