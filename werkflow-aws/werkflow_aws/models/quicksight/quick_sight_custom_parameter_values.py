from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightCustomParameterValues(BaseModel):
    StringValues: list[StrictStr] | None = None
    IntegerValues: list[StrictInt] | None = None
    DecimalValues: list[StrictFloat | StrictInt] | None = None
    DateTimeValues: list[datetime.datetime | StrictStr] | None = None
