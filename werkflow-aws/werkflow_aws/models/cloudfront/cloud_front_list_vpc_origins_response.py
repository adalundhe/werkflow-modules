from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_vpc_origin_list import CloudFrontVpcOriginList


class CloudFrontListVpcOriginsResponse(BaseModel):
    VpcOriginList: CloudFrontVpcOriginList | None = None
    ResponseMetadata: dict[str, Any] | None = None
