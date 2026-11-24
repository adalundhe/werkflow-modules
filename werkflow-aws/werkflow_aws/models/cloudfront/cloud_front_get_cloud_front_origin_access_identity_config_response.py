from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_identity_config import CloudFrontOriginAccessIdentityConfig as _CloudFrontOriginAccessIdentityConfigType


class CloudFrontGetCloudFrontOriginAccessIdentityConfigResponse(BaseModel):
    CloudFrontOriginAccessIdentityConfig: _CloudFrontOriginAccessIdentityConfigType | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
