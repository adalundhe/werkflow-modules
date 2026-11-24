from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRListImagesResponse(BaseModel):
    imageIds: list[ECRImageIdentifier] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
