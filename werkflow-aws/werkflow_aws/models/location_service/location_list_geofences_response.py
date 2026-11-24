from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_geofence_response_entry import LocationListGeofenceResponseEntry


class LocationListGeofencesResponse(BaseModel):
    Entries: list[LocationListGeofenceResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
