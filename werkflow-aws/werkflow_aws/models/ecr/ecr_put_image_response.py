from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_image import ECRImage


class ECRPutImageResponse(BaseModel):
    image: ECRImage | None = None
    ResponseMetadata: dict[str, Any] | None = None
