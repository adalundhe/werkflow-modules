from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightLineChartLineStyleSettings(BaseModel):
    LineVisibility: StrictStr | None = None
    LineInterpolation: StrictStr | None = None
    LineStyle: StrictStr | None = None
    LineWidth: StrictStr | None = None
