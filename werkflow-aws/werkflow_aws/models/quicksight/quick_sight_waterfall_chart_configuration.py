from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette
from .quick_sight_waterfall_chart_color_configuration import QuickSightWaterfallChartColorConfiguration
from .quick_sight_waterfall_chart_field_wells import QuickSightWaterfallChartFieldWells
from .quick_sight_waterfall_chart_options import QuickSightWaterfallChartOptions
from .quick_sight_waterfall_chart_sort_configuration import QuickSightWaterfallChartSortConfiguration


class QuickSightWaterfallChartConfiguration(BaseModel):
    FieldWells: QuickSightWaterfallChartFieldWells | None = None
    SortConfiguration: QuickSightWaterfallChartSortConfiguration | None = None
    WaterfallChartOptions: QuickSightWaterfallChartOptions | None = None
    CategoryAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    CategoryAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    PrimaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    PrimaryYAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    ColorConfiguration: QuickSightWaterfallChartColorConfiguration | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
