from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_instance_access_details import LightsailInstanceAccessDetails


class LightsailGetInstanceAccessDetailsResponse(BaseModel):
    accessDetails: LightsailInstanceAccessDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
