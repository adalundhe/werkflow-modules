from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_delete_geofence_error import LocationBatchDeleteGeofenceError


class LocationBatchDeleteGeofenceResponse(BaseModel):
    Errors: list[LocationBatchDeleteGeofenceError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
