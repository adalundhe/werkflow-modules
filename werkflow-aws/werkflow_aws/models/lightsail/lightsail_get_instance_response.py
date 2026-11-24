from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_instance import LightsailInstance


class LightsailGetInstanceResponse(BaseModel):
    instance: LightsailInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
