from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightWaterfallChartOptions(BaseModel):
    TotalBarLabel: StrictStr | None = None
