from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightYAxisOptions(BaseModel):
    YAxis: StrictStr | None = None
