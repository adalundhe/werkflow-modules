from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_heatmap_color_scale import QuickSightGeospatialHeatmapColorScale


class QuickSightGeospatialHeatmapConfiguration(BaseModel):
    HeatmapColor: QuickSightGeospatialHeatmapColorScale | None = None
