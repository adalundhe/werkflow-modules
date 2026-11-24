from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_funnel_chart_data_label_options import QuickSightFunnelChartDataLabelOptions
from .quick_sight_funnel_chart_field_wells import QuickSightFunnelChartFieldWells
from .quick_sight_funnel_chart_sort_configuration import QuickSightFunnelChartSortConfiguration
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightFunnelChartConfiguration(BaseModel):
    FieldWells: QuickSightFunnelChartFieldWells | None = None
    SortConfiguration: QuickSightFunnelChartSortConfiguration | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ValueLabelOptions: QuickSightChartAxisLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    DataLabelOptions: QuickSightFunnelChartDataLabelOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
