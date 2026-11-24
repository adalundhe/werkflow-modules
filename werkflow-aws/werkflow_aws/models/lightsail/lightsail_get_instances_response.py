from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_instance import LightsailInstance


class LightsailGetInstancesResponse(BaseModel):
    instances: list[LightsailInstance] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
