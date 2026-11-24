from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGaugeChartColorConfiguration(BaseModel):
    ForegroundColor: StrictStr | None = None
    BackgroundColor: StrictStr | None = None
