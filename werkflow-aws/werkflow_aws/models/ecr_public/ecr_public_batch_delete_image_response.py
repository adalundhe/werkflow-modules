from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_image_failure import ECRPublicImageFailure
from .ecr_public_image_identifier import ECRPublicImageIdentifier


class ECRPublicBatchDeleteImageResponse(BaseModel):
    imageIds: list[ECRPublicImageIdentifier] | None = None
    failures: list[ECRPublicImageFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
