from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_identity_config import CloudFrontOriginAccessIdentityConfig as _CloudFrontOriginAccessIdentityConfigType


class CloudFrontUpdateCloudFrontOriginAccessIdentityRequest(BaseModel):
    CloudFrontOriginAccessIdentityConfig: _CloudFrontOriginAccessIdentityConfigType
    Id: StrictStr
    IfMatch: StrictStr | None = None
