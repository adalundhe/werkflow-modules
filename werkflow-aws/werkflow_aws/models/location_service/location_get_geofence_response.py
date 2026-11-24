from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_geofence_geometry import LocationGeofenceGeometry


class LocationGetGeofenceResponse(BaseModel):
    GeofenceId: StrictStr | None = None
    Geometry: LocationGeofenceGeometry | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    GeofenceProperties: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
