from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_container_image import LightsailContainerImage


class LightsailRegisterContainerImageResponse(BaseModel):
    containerImage: LightsailContainerImage | None = None
    ResponseMetadata: dict[str, Any] | None = None
