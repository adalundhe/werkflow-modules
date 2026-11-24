from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_origin_access_control_list import CloudFrontOriginAccessControlList


class CloudFrontListOriginAccessControlsResponse(BaseModel):
    OriginAccessControlList: CloudFrontOriginAccessControlList | None = None
    ResponseMetadata: dict[str, Any] | None = None
