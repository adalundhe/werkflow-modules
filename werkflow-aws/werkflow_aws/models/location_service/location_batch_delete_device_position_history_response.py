from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .location_batch_delete_device_position_history_error import LocationBatchDeleteDevicePositionHistoryError


class LocationBatchDeleteDevicePositionHistoryResponse(BaseModel):
    Errors: list[LocationBatchDeleteDevicePositionHistoryError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
