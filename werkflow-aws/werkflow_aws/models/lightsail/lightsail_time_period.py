from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailTimePeriod(BaseModel):
    start: datetime.datetime | StrictStr | None = None
    end: datetime.datetime | StrictStr | None = None
