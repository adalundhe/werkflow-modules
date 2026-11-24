from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_instance_state import LightsailInstanceState


class LightsailGetInstanceStateResponse(BaseModel):
    state: LightsailInstanceState | None = None
    ResponseMetadata: dict[str, Any] | None = None
