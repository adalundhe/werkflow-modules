from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_color import QuickSightDataColor


class QuickSightColorScale(BaseModel):
    Colors: list[QuickSightDataColor] | None = None
    ColorFillType: StrictStr | None = None
    NullValueColor: QuickSightDataColor | None = None
