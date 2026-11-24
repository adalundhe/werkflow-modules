from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_invalidation import CloudFrontInvalidation


class CloudFrontCreateInvalidationResponse(BaseModel):
    Location: StrictStr | None = None
    Invalidation: CloudFrontInvalidation | None = None
    ResponseMetadata: dict[str, Any] | None = None
