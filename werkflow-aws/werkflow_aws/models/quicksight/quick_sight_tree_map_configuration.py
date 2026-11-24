from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_chart_axis_label_options import QuickSightChartAxisLabelOptions
from .quick_sight_color_scale import QuickSightColorScale
from .quick_sight_data_label_options import QuickSightDataLabelOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_tree_map_field_wells import QuickSightTreeMapFieldWells
from .quick_sight_tree_map_sort_configuration import QuickSightTreeMapSortConfiguration
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightTreeMapConfiguration(BaseModel):
    FieldWells: QuickSightTreeMapFieldWells | None = None
    SortConfiguration: QuickSightTreeMapSortConfiguration | None = None
    GroupLabelOptions: QuickSightChartAxisLabelOptions | None = None
    SizeLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColorLabelOptions: QuickSightChartAxisLabelOptions | None = None
    ColorScale: QuickSightColorScale | None = None
    Legend: QuickSightLegendOptions | None = None
    DataLabels: QuickSightDataLabelOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
