from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2ScanResultConditionRequest(BaseModel):
    MaxDaysSinceLastFindingScan: StrictInt | None = None
    MaximumSeverityLabel: Literal['informational', 'low', 'medium', 'high', 'critical'] | None = None
    MaxDaysSinceInformationalFixAvailable: StrictInt | None = None
    MaxDaysSinceLowFixAvailable: StrictInt | None = None
    MaxDaysSinceMediumFixAvailable: StrictInt | None = None
    MaxDaysSinceHighFixAvailable: StrictInt | None = None
    MaxDaysSinceCriticalFixAvailable: StrictInt | None = None
