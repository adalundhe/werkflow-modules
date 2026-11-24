from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLineChartMarkerStyleSettings(BaseModel):
    MarkerVisibility: StrictStr | None = None
    MarkerShape: StrictStr | None = None
    MarkerSize: StrictStr | None = None
    MarkerColor: StrictStr | None = None
