from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_list_device_positions_response_entry import LocationListDevicePositionsResponseEntry


class LocationListDevicePositionsResponse(BaseModel):
    Entries: list[LocationListDevicePositionsResponseEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
