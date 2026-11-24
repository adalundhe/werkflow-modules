from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2CreationDateCondition(BaseModel):
    MaximumDaysSinceCreated: StrictInt | None = None
