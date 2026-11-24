from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailRefreshScheduleFrequency(BaseModel):
    Unit: StrictStr | None = None
    Value: StrictInt | None = None
