from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightNewDefaultValues(BaseModel):
    StringStaticValues: list[StrictStr] | None = None
    DecimalStaticValues: list[StrictFloat | StrictInt] | None = None
    DateTimeStaticValues: list[datetime.datetime | StrictStr] | None = None
    IntegerStaticValues: list[StrictInt] | None = None
