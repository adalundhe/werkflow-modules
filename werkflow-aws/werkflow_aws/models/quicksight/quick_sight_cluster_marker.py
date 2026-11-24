from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_simple_cluster_marker import QuickSightSimpleClusterMarker


class QuickSightClusterMarker(BaseModel):
    SimpleClusterMarker: QuickSightSimpleClusterMarker | None = None
