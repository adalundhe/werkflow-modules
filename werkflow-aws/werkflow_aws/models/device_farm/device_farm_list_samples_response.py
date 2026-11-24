from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_sample import DeviceFarmSample


class DeviceFarmListSamplesResponse(BaseModel):
    samples: list[DeviceFarmSample] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
