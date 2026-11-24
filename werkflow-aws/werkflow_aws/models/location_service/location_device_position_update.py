from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .location_positional_accuracy import LocationPositionalAccuracy


class LocationDevicePositionUpdate(BaseModel):
    DeviceId: StrictStr
    SampleTime: datetime.datetime | StrictStr
    Position: list[StrictFloat | StrictInt]
    Accuracy: LocationPositionalAccuracy | None = None
    PositionProperties: dict[StrictStr, StrictStr] | None = None
