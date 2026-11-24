from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class AutoScalingCapacityForecast(BaseModel):
    Timestamps: list[datetime.datetime | StrictStr] | None = None
    Values: list[StrictFloat | StrictInt] | None = None
