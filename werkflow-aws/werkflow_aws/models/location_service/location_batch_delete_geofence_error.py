from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_batch_item_error import LocationBatchItemError


class LocationBatchDeleteGeofenceError(BaseModel):
    GeofenceId: StrictStr | None = None
    Error: LocationBatchItemError | None = None
