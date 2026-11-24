from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_cluster_marker_configuration import QuickSightClusterMarkerConfiguration
from .quick_sight_geospatial_heatmap_configuration import QuickSightGeospatialHeatmapConfiguration


class QuickSightGeospatialPointStyleOptions(BaseModel):
    SelectedPointStyle: StrictStr | None = None
    ClusterMarkerConfiguration: QuickSightClusterMarkerConfiguration | None = None
    HeatmapConfiguration: QuickSightGeospatialHeatmapConfiguration | None = None
