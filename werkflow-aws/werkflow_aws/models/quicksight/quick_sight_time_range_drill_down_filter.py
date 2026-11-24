from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightTimeRangeDrillDownFilter(BaseModel):
    Column: QuickSightColumnIdentifier | None = None
    RangeMinimum: datetime.datetime | StrictStr | None = None
    RangeMaximum: datetime.datetime | StrictStr | None = None
    TimeGranularity: StrictStr | None = None
