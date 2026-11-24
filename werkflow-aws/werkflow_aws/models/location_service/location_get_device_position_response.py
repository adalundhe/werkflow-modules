from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .location_positional_accuracy import LocationPositionalAccuracy


class LocationGetDevicePositionResponse(BaseModel):
    DeviceId: StrictStr | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
    ReceivedTime: datetime.datetime | StrictStr | None = None
    Position: list[StrictFloat | StrictInt] | None = None
    Accuracy: LocationPositionalAccuracy | None = None
    PositionProperties: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
