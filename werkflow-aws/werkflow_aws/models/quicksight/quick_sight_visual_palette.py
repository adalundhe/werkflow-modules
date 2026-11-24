from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_color import QuickSightDataPathColor


class QuickSightVisualPalette(BaseModel):
    ChartColor: StrictStr | None = None
    ColorMap: list[QuickSightDataPathColor] | None = None
