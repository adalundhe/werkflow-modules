from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_offering import DeviceFarmOffering


class DeviceFarmListOfferingsResponse(BaseModel):
    offerings: list[DeviceFarmOffering] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
