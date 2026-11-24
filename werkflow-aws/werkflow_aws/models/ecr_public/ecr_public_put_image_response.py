from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_image import ECRPublicImage


class ECRPublicPutImageResponse(BaseModel):
    image: ECRPublicImage | None = None
    ResponseMetadata: dict[str, Any] | None = None
