from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_box_plot_field_wells import QuickSightBoxPlotFieldWells
from .quick_sight_box_plot_options import QuickSightBoxPlotOptions
from .quick_sight_box_plot_sort_configuration import QuickSightBoxPlotSortConfiguration
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_reference_line import QuickSightReferenceLine
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightBoxPlotChartConfiguration(BaseModel):
    FieldWells: QuickSightBoxPlotFieldWells | None = None
    SortConfiguration: QuickSightBoxPlotSortConfiguration | None = None
    BoxPlotOptions: QuickSightBoxPlotOptions | None = None
    CategoryAxis: QuickSightAxisDisplayOptions | None = None
    CategoryLabelOptions: QuickSightChartAxisLabelOptions | None = None
    PrimaryYAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    PrimaryYAxisLabelOptions: QuickSightChartAxisLabelOptions | None = None
    Legend: QuickSightLegendOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    ReferenceLines: list[QuickSightReferenceLine] | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
