from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class CloudWatchWarmUpConfiguration(BaseModel):
    WarmUpPeriodDurationInMinutes: StrictInt | None = None
    OnlyStartEvaluatingAfterWarmUpPeriodEnds: StrictBool | None = None
