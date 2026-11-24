from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_invalidation_list import CloudFrontInvalidationList


class CloudFrontListInvalidationsResponse(BaseModel):
    InvalidationList: CloudFrontInvalidationList | None = None
    ResponseMetadata: dict[str, Any] | None = None
