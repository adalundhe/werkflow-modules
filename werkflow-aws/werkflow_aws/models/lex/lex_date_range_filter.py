from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexDateRangeFilter(BaseModel):
    startDateTime: datetime.datetime | StrictStr | None = None
    endDateTime: datetime.datetime | StrictStr | None = None
