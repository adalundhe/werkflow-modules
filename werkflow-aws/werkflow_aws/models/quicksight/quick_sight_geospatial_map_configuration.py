from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_map_field_wells import QuickSightGeospatialMapFieldWells
from .quick_sight_geospatial_map_style_options import QuickSightGeospatialMapStyleOptions
from .quick_sight_geospatial_point_style_options import QuickSightGeospatialPointStyleOptions
from .quick_sight_geospatial_window_options import QuickSightGeospatialWindowOptions
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_tooltip_options import QuickSightTooltipOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions
from .quick_sight_visual_palette import QuickSightVisualPalette


class QuickSightGeospatialMapConfiguration(BaseModel):
    FieldWells: QuickSightGeospatialMapFieldWells | None = None
    Legend: QuickSightLegendOptions | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    WindowOptions: QuickSightGeospatialWindowOptions | None = None
    MapStyleOptions: QuickSightGeospatialMapStyleOptions | None = None
    PointStyleOptions: QuickSightGeospatialPointStyleOptions | None = None
    VisualPalette: QuickSightVisualPalette | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
