from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ResilienceHubFailurePolicy(BaseModel):
    rpoInSecs: StrictInt | None = None
    rtoInSecs: StrictInt | None = None
