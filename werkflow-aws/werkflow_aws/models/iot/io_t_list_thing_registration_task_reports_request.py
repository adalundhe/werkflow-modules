from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListThingRegistrationTaskReportsRequest(BaseModel):
    taskId: StrictStr
    reportType: Literal['ERRORS', 'RESULTS']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
