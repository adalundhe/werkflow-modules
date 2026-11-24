from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .location_batch_item_error import LocationBatchItemError


class LocationBatchDeleteDevicePositionHistoryError(BaseModel):
    DeviceId: StrictStr | None = None
    Error: LocationBatchItemError | None = None
