from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_offering_status import DeviceFarmOfferingStatus


class DeviceFarmGetOfferingStatusResponse(BaseModel):
    current: dict[StrictStr, DeviceFarmOfferingStatus] | None = None
    nextPeriod: dict[StrictStr, DeviceFarmOfferingStatus] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
