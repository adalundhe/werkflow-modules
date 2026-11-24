from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2DeprecationTimeConditionRequest(BaseModel):
    MaximumDaysSinceDeprecated: StrictInt | None = None
