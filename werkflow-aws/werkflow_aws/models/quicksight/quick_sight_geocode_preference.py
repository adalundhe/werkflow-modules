from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geocode_preference_value import QuickSightGeocodePreferenceValue
from .quick_sight_geocoder_hierarchy import QuickSightGeocoderHierarchy


class QuickSightGeocodePreference(BaseModel):
    RequestKey: QuickSightGeocoderHierarchy | None = None
    Preference: QuickSightGeocodePreferenceValue | None = None
