from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_tag import DeviceFarmTag


class DeviceFarmListTagsForResourceResponse(BaseModel):
    Tags: list[DeviceFarmTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
