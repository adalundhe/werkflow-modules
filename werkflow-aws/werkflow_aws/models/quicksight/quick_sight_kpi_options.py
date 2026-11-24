from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_comparison_configuration import QuickSightComparisonConfiguration
from .quick_sight_font_configuration import QuickSightFontConfiguration
from .quick_sight_kpi_sparkline_options import QuickSightKPISparklineOptions
from .quick_sight_kpi_visual_layout_options import QuickSightKPIVisualLayoutOptions
from .quick_sight_progress_bar_options import QuickSightProgressBarOptions
from .quick_sight_secondary_value_options import QuickSightSecondaryValueOptions
from .quick_sight_trend_arrow_options import QuickSightTrendArrowOptions


class QuickSightKPIOptions(BaseModel):
    ProgressBar: QuickSightProgressBarOptions | None = None
    TrendArrows: QuickSightTrendArrowOptions | None = None
    SecondaryValue: QuickSightSecondaryValueOptions | None = None
    Comparison: QuickSightComparisonConfiguration | None = None
    PrimaryValueDisplayType: StrictStr | None = None
    PrimaryValueFontConfiguration: QuickSightFontConfiguration | None = None
    SecondaryValueFontConfiguration: QuickSightFontConfiguration | None = None
    Sparkline: QuickSightKPISparklineOptions | None = None
    VisualLayoutOptions: QuickSightKPIVisualLayoutOptions | None = None
