from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightDataSetDateFilterValue(BaseModel):
    StaticValue: datetime.datetime | StrictStr | None = None
