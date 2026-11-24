from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_device_position import LocationDevicePosition


class LocationGetDevicePositionHistoryResponse(BaseModel):
    DevicePositions: list[LocationDevicePosition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
