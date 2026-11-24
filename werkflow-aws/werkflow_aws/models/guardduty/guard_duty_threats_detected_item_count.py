from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyThreatsDetectedItemCount(BaseModel):
    Files: StrictInt | None = None
