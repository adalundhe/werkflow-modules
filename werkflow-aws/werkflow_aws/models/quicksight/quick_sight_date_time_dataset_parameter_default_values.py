from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDateTimeDatasetParameterDefaultValues(BaseModel):
    StaticValues: list[datetime.datetime | StrictStr] | None = None
