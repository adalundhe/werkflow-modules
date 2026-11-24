from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConfigServiceSsmControls(BaseModel):
    ConcurrentExecutionRatePercentage: StrictInt | None = None
    ErrorPercentage: StrictInt | None = None
