from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTJobsDataGetPendingJobExecutionsRequest(BaseModel):
    thingName: StrictStr
