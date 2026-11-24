from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBoxPlotStyleOptions(BaseModel):
    FillStyle: StrictStr | None = None
