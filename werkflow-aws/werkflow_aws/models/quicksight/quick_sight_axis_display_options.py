from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_data_options import QuickSightAxisDataOptions
from .quick_sight_axis_tick_label_options import QuickSightAxisTickLabelOptions
from .quick_sight_scroll_bar_options import QuickSightScrollBarOptions


class QuickSightAxisDisplayOptions(BaseModel):
    TickLabelOptions: QuickSightAxisTickLabelOptions | None = None
    AxisLineVisibility: StrictStr | None = None
    GridLineVisibility: StrictStr | None = None
    DataOptions: QuickSightAxisDataOptions | None = None
    ScrollbarOptions: QuickSightScrollBarOptions | None = None
    AxisOffset: StrictStr | None = None
