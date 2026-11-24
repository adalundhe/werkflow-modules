from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .location_geofence_geometry import LocationGeofenceGeometry


class LocationListGeofenceResponseEntry(BaseModel):
    GeofenceId: StrictStr | None = None
    Geometry: LocationGeofenceGeometry | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    GeofenceProperties: dict[StrictStr, StrictStr] | None = None
