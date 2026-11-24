from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_line_layer import QuickSightGeospatialLineLayer
from .quick_sight_geospatial_point_layer import QuickSightGeospatialPointLayer
from .quick_sight_geospatial_polygon_layer import QuickSightGeospatialPolygonLayer


class QuickSightGeospatialLayerDefinition(BaseModel):
    PointLayer: QuickSightGeospatialPointLayer | None = None
    LineLayer: QuickSightGeospatialLineLayer | None = None
    PolygonLayer: QuickSightGeospatialPolygonLayer | None = None
