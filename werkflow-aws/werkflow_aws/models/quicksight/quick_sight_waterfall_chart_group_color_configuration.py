from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightWaterfallChartGroupColorConfiguration(BaseModel):
    PositiveBarColor: StrictStr | None = None
    NegativeBarColor: StrictStr | None = None
    TotalBarColor: StrictStr | None = None
