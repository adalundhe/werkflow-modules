from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_access_identity_config import CloudFrontOriginAccessIdentityConfig as _CloudFrontOriginAccessIdentityConfigType


class CloudFrontOriginAccessIdentity(BaseModel):
    Id: StrictStr | None = None
    S3CanonicalUserId: StrictStr | None = None
    CloudFrontOriginAccessIdentityConfig: _CloudFrontOriginAccessIdentityConfigType | None = None
