from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_public_image_detail import ECRPublicImageDetail


class ECRPublicDescribeImagesResponse(BaseModel):
    imageDetails: list[ECRPublicImageDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
