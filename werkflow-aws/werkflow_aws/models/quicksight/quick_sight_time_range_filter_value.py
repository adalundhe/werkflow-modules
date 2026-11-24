from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_rolling_date_configuration import QuickSightRollingDateConfiguration


class QuickSightTimeRangeFilterValue(BaseModel):
    StaticValue: datetime.datetime | StrictStr | None = None
    RollingDate: QuickSightRollingDateConfiguration | None = None
    Parameter: StrictStr | None = None
