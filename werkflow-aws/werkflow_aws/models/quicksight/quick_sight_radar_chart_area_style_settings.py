from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRadarChartAreaStyleSettings(BaseModel):
    Visibility: StrictStr | None = None
