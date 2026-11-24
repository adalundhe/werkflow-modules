from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectIntervalDetails(BaseModel):
    TimeZone: StrictStr | None = None
    IntervalPeriod: Literal['FIFTEEN_MIN', 'THIRTY_MIN', 'HOUR', 'DAY', 'WEEK', 'TOTAL'] | None = None
