from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GlueDateColumnStatisticsData(BaseModel):
    MinimumValue: datetime.datetime | StrictStr | None = None
    MaximumValue: datetime.datetime | StrictStr | None = None
    NumberOfNulls: StrictInt | None = None
    NumberOfDistinctValues: StrictInt | None = None
