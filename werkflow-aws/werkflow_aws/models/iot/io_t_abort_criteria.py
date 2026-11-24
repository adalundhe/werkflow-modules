from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class IoTAbortCriteria(BaseModel):
    failureType: StrictStr | None = None
    action: StrictStr | None = None
    thresholdPercentage: StrictFloat | StrictInt | None = None
    minNumberOfExecutedThings: StrictInt | None = None
