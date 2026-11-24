from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_layer_item import QuickSightGeospatialLayerItem
from .quick_sight_geospatial_map_state import QuickSightGeospatialMapState
from .quick_sight_geospatial_map_style import QuickSightGeospatialMapStyle
from .quick_sight_legend_options import QuickSightLegendOptions
from .quick_sight_visual_interaction_options import QuickSightVisualInteractionOptions


class QuickSightGeospatialLayerMapConfiguration(BaseModel):
    Legend: QuickSightLegendOptions | None = None
    MapLayers: list[QuickSightGeospatialLayerItem] | None = None
    MapState: QuickSightGeospatialMapState | None = None
    MapStyle: QuickSightGeospatialMapStyle | None = None
    Interactions: QuickSightVisualInteractionOptions | None = None
