from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .location_batch_item_error import LocationBatchItemError


class LocationBatchUpdateDevicePositionError(BaseModel):
    DeviceId: StrictStr | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
    Error: LocationBatchItemError | None = None
