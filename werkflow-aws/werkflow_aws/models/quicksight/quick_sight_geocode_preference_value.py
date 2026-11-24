from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_coordinate import QuickSightCoordinate
from .quick_sight_geocoder_hierarchy import QuickSightGeocoderHierarchy


class QuickSightGeocodePreferenceValue(BaseModel):
    GeocoderHierarchy: QuickSightGeocoderHierarchy | None = None
    Coordinate: QuickSightCoordinate | None = None
