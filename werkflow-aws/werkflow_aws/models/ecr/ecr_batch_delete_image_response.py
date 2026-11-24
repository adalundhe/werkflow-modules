from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_image_failure import ECRImageFailure
from .ecr_image_identifier import ECRImageIdentifier


class ECRBatchDeleteImageResponse(BaseModel):
    imageIds: list[ECRImageIdentifier] | None = None
    failures: list[ECRImageFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
