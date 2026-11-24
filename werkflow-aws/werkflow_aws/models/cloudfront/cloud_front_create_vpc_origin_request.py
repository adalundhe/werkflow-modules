from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_tags import CloudFrontTags
from .cloud_front_vpc_origin_endpoint_config import CloudFrontVpcOriginEndpointConfig


class CloudFrontCreateVpcOriginRequest(BaseModel):
    VpcOriginEndpointConfig: CloudFrontVpcOriginEndpointConfig
    Tags: CloudFrontTags | None = None
