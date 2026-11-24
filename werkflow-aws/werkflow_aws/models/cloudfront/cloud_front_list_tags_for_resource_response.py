from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_tags import CloudFrontTags


class CloudFrontListTagsForResourceResponse(BaseModel):
    Tags: CloudFrontTags | None = None
    ResponseMetadata: dict[str, Any] | None = None
