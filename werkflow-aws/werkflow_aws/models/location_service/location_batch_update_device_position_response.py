from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_update_device_position_error import LocationBatchUpdateDevicePositionError


class LocationBatchUpdateDevicePositionResponse(BaseModel):
    Errors: list[LocationBatchUpdateDevicePositionError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
