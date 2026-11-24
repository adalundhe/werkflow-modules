from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_gauge_chart_color_configuration import QuickSightGaugeChartColorConfiguration
from .quick_sight_gauge_chart_field_wells import QuickSightGaugeChartFieldWells
from .quick_sight_gauge_chart_options import QuickSightGaugeChartOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightGaugeChartConfiguration(BaseModel):
    FieldWells: QuickSightGaugeChartFieldWells | None = None
    GaugeChartOptions: QuickSightGaugeChartOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    TooltipOptions: QuickSightTooltipOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    ColorConfiguration: QuickSightGaugeChartColorConfiguration | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
