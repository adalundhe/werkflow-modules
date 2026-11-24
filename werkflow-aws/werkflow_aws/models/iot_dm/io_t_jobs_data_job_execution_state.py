from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobsDataJobExecutionState(BaseModel):
    status: StrictStr | None = None
    statusDetails: dict[StrictStr, StrictStr] | None = None
    versionNumber: StrictInt | None = None
