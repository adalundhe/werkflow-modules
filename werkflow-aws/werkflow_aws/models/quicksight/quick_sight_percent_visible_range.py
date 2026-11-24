from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightPercentVisibleRange(BaseModel):
    From: StrictFloat | StrictInt | None = None
    To: StrictFloat | StrictInt | None = None
