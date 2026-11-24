from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListThingRegistrationTasksRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    status: Literal['InProgress', 'Completed', 'Failed', 'Cancelled', 'Cancelling'] | None = None
