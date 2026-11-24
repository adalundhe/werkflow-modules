from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_upload import DeviceFarmUpload


class DeviceFarmListUploadsResponse(BaseModel):
    uploads: list[DeviceFarmUpload] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
