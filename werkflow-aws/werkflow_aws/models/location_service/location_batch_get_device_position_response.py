from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_get_device_position_error import LocationBatchGetDevicePositionError
from .location_device_position import LocationDevicePosition


class LocationBatchGetDevicePositionResponse(BaseModel):
    Errors: list[LocationBatchGetDevicePositionError] | None = None
    DevicePositions: list[LocationDevicePosition] | None = None
    ResponseMetadata: dict[str, Any] | None = None
