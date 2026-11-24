from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_heatmap_data_color import QuickSightGeospatialHeatmapDataColor


class QuickSightGeospatialHeatmapColorScale(BaseModel):
    Colors: list[QuickSightGeospatialHeatmapDataColor] | None = None
