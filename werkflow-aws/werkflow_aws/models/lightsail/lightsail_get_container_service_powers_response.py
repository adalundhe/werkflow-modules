from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_container_service_power import LightsailContainerServicePower


class LightsailGetContainerServicePowersResponse(BaseModel):
    powers: list[LightsailContainerServicePower] | None = None
    ResponseMetadata: dict[str, Any] | None = None
