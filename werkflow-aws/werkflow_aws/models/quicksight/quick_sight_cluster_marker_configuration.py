from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_cluster_marker import QuickSightClusterMarker


class QuickSightClusterMarkerConfiguration(BaseModel):
    ClusterMarker: QuickSightClusterMarker | None = None
