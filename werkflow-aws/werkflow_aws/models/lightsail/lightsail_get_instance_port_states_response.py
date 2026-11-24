from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_instance_port_state import LightsailInstancePortState


class LightsailGetInstancePortStatesResponse(BaseModel):
    portStates: list[LightsailInstancePortState] | None = None
    ResponseMetadata: dict[str, Any] | None = None
