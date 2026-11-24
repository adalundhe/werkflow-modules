from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_arc_axis_configuration import QuickSightArcAxisConfiguration
from .quick_sight_arc_configuration import QuickSightArcConfiguration
from .quick_sight_comparison_configuration import QuickSightComparisonConfiguration
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightGaugeChartOptions(BaseModel):
    PrimaryValueDisplayType: StrictStr | None = None
    Comparison: QuickSightComparisonConfiguration | None = None
    ArcAxis: QuickSightArcAxisConfiguration | None = None
    Arc: QuickSightArcConfiguration | None = None
    PrimaryValueFontConfiguration: QuickSightFontConfiguration | None = None
