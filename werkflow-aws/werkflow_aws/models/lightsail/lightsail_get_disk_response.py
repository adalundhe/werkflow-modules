from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_disk import LightsailDisk


class LightsailGetDiskResponse(BaseModel):
    disk: LightsailDisk | None = None
    ResponseMetadata: dict[str, Any] | None = None
