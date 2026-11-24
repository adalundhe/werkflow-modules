from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_geofence_geometry import LocationGeofenceGeometry


class LocationBatchPutGeofenceRequestEntry(BaseModel):
    GeofenceId: StrictStr
    Geometry: LocationGeofenceGeometry
    GeofenceProperties: dict[StrictStr, StrictStr] | None = None
