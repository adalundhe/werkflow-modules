from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_put_geofence_error import LocationBatchPutGeofenceError
from .location_batch_put_geofence_success import LocationBatchPutGeofenceSuccess


class LocationBatchPutGeofenceResponse(BaseModel):
    Successes: list[LocationBatchPutGeofenceSuccess] | None = None
    Errors: list[LocationBatchPutGeofenceError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
