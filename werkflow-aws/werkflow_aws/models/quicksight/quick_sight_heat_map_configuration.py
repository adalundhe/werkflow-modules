from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_color_scale import QuickSightColorScale
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_heat_map_field_wells import QuickSightHeatMapFieldWells
from .quick_sight_heat_map_sort_configuration import QuickSightHeatMapSortConfiguration
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightHeatMapConfiguration(BaseModel):
    FieldWells: QuickSightHeatMapFieldWells | None = None
    SortConfiguration: QuickSightHeatMapSortConfiguration | None = None
    RowAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    RowLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColumnAxisDisplayOptions: QuickSightAxisDisplayOptions | None = None
    ColumnLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColorScale: QuickSightColorScale | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
