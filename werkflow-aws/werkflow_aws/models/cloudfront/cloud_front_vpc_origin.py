from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_vpc_origin_endpoint_config import CloudFrontVpcOriginEndpointConfig


class CloudFrontVpcOrigin(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    AccountId: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    VpcOriginEndpointConfig: CloudFrontVpcOriginEndpointConfig | None = None
