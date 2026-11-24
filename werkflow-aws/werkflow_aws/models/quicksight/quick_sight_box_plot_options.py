from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_box_plot_style_options import QuickSightBoxPlotStyleOptions


class QuickSightBoxPlotOptions(BaseModel):
    StyleOptions: QuickSightBoxPlotStyleOptions | None = None
    OutlierVisibility: StrictStr | None = None
    AllDataPointsVisibility: StrictStr | None = None
