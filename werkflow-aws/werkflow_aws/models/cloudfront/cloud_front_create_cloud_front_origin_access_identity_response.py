from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_identity import CloudFrontOriginAccessIdentity as _CloudFrontOriginAccessIdentityType


class CloudFrontCreateCloudFrontOriginAccessIdentityResponse(BaseModel):
    CloudFrontOriginAccessIdentity: _CloudFrontOriginAccessIdentityType | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
