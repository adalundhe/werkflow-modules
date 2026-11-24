from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_batch_put_geofence_request_entry import LocationBatchPutGeofenceRequestEntry


class LocationBatchPutGeofenceRequest(BaseModel):
    CollectionName: StrictStr
    Entries: list[LocationBatchPutGeofenceRequestEntry]
