from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_inferred_state import LocationInferredState


class LocationVerifyDevicePositionResponse(BaseModel):
    InferredState: LocationInferredState | None = None
    DeviceId: StrictStr | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
    ReceivedTime: datetime.datetime | StrictStr | None = None
    DistanceUnit: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
