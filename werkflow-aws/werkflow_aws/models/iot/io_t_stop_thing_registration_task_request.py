from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStopThingRegistrationTaskRequest(BaseModel):
    taskId: StrictStr
