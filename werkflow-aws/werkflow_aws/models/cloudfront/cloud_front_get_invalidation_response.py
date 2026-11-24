from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_invalidation import CloudFrontInvalidation


class CloudFrontGetInvalidationResponse(BaseModel):
    Invalidation: CloudFrontInvalidation | None = None
    ResponseMetadata: dict[str, Any] | None = None
