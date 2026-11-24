from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2DeprecationTimeCondition(BaseModel):
    MaximumDaysSinceDeprecated: StrictInt | None = None
