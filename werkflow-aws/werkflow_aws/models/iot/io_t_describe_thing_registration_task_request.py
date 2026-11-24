from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeThingRegistrationTaskRequest(BaseModel):
    taskId: StrictStr
