from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_disk import LightsailDisk


class LightsailGetDisksResponse(BaseModel):
    disks: list[LightsailDisk] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
