from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectHoursOfOperationTimeSlice(BaseModel):
    Hours: StrictInt | None = None
    Minutes: StrictInt | None = None
