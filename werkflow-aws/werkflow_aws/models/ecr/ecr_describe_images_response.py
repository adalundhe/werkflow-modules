from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_detail import ECRImageDetail


class ECRDescribeImagesResponse(BaseModel):
    imageDetails: list[ECRImageDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
