from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_geofence_collections_response_entry import LocationListGeofenceCollectionsResponseEntry


class LocationListGeofenceCollectionsResponse(BaseModel):
    Entries: list[LocationListGeofenceCollectionsResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
