from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_container_service import LightsailContainerService


class LightsailCreateContainerServiceResponse(BaseModel):
    containerService: LightsailContainerService | None = None
    ResponseMetadata: dict[str, Any] | None = None
