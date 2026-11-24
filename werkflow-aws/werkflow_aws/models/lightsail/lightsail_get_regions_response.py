from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_region import LightsailRegion


class LightsailGetRegionsResponse(BaseModel):
    regions: list[LightsailRegion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
