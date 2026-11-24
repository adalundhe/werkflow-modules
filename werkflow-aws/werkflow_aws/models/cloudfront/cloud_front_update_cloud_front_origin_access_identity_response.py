from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_identity import CloudFrontOriginAccessIdentity as _CloudFrontOriginAccessIdentityType


class CloudFrontUpdateCloudFrontOriginAccessIdentityResponse(BaseModel):
    CloudFrontOriginAccessIdentity: _CloudFrontOriginAccessIdentityType | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
