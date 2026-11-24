from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDateTimeParameter(BaseModel):
    Name: StrictStr | None = None
    Values: list[datetime.datetime | StrictStr] | None = None
