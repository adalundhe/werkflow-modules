from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ScanResultCondition(BaseModel):
    MaxDaysSinceLastFindingScan: StrictInt | None = None
    MaximumSeverityLabel: StrictStr | None = None
    MaxDaysSinceInformationalFixAvailable: StrictInt | None = None
    MaxDaysSinceLowFixAvailable: StrictInt | None = None
    MaxDaysSinceMediumFixAvailable: StrictInt | None = None
    MaxDaysSinceHighFixAvailable: StrictInt | None = None
    MaxDaysSinceCriticalFixAvailable: StrictInt | None = None
