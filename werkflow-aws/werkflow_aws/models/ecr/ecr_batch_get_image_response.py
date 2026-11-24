from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_image import ECRImage
from .ecr_image_failure import ECRImageFailure


class ECRBatchGetImageResponse(BaseModel):
    images: list[ECRImage] | None = None
    failures: list[ECRImageFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
