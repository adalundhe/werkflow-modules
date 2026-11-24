from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_vpc_origin_endpoint_config import CloudFrontVpcOriginEndpointConfig


class CloudFrontUpdateVpcOriginRequest(BaseModel):
    VpcOriginEndpointConfig: CloudFrontVpcOriginEndpointConfig
    Id: StrictStr
    IfMatch: StrictStr
