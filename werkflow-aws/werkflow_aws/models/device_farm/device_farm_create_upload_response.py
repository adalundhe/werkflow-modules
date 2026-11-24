from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_upload import DeviceFarmUpload


class DeviceFarmCreateUploadResponse(BaseModel):
    upload: DeviceFarmUpload | None = None
    ResponseMetadata: dict[str, Any] | None = None
