from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_public_image_tag_detail import ECRPublicImageTagDetail


class ECRPublicDescribeImageTagsResponse(BaseModel):
    imageTagDetails: list[ECRPublicImageTagDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
