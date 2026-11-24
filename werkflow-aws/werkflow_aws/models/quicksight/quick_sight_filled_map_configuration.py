from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_filled_map_field_wells import QuickSightFilledMapFieldWells
from .quick_sight_filled_map_sort_configuration import QuickSightFilledMapSortConfiguration
from .quick_sight_geospatial_map_style_options import QuickSightGeospatialMapStyleOptions
from .quick_sight_geospatial_window_options import QuickSightGeospatialWindowOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightFilledMapConfiguration(BaseModel):
    FieldWells: QuickSightFilledMapFieldWells | None = None
    SortConfiguration: QuickSightFilledMapSortConfiguration | None = None
    Legend: QuickSightLegendOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    WindowOptions: QuickSightGeospatialWindowOptions | None = None
    MapStyleOptions: QuickSightGeospatialMapStyleOptions | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
