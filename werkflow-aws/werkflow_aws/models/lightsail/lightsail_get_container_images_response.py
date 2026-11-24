from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_container_image import LightsailContainerImage


class LightsailGetContainerImagesResponse(BaseModel):
    containerImages: list[LightsailContainerImage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
