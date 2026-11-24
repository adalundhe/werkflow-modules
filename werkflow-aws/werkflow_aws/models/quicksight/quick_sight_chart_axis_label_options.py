from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_label_options import QuickSightAxisLabelOptions


class QuickSightChartAxisLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    SortIconVisibility: StrictStr | None = None
    AxisLabelOptions: list[QuickSightAxisLabelOptions] | None = None
