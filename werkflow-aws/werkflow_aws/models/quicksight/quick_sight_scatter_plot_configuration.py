from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_scatter_plot_field_wells import QuickSightScatterPlotFieldWells
from .quick_sight_scatter_plot_sort_configuration import QuickSightScatterPlotSortConfiguration
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightScatterPlotConfiguration(BaseModel):
    FieldWells: QuickSightScatterPlotFieldWells | None = None
    SortConfiguration: QuickSightScatterPlotSortConfiguration | None = None
    XAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    XAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    YAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    YAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
