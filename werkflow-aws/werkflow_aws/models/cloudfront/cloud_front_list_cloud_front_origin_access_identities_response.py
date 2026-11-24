from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_origin_access_identity_list import CloudFrontOriginAccessIdentityList as _CloudFrontOriginAccessIdentityListType


class CloudFrontListCloudFrontOriginAccessIdentitiesResponse(BaseModel):
    CloudFrontOriginAccessIdentityList: _CloudFrontOriginAccessIdentityListType | None = None
    ResponseMetadata: dict[str, Any] | None = None
