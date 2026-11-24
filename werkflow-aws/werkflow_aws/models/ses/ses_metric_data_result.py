from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SESMetricDataResult(BaseModel):
    Id: StrictStr | None = None
    Timestamps: list[datetime.datetime | StrictStr] | None = None
    Values: list[StrictInt] | None = None
