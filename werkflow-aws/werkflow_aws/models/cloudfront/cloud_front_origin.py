from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_custom_headers import CloudFrontCustomHeaders
from .cloud_front_custom_origin_config import CloudFrontCustomOriginConfig
from .cloud_front_origin_shield import CloudFrontOriginShield
from .cloud_front_s3_origin_config import CloudFrontS3OriginConfig
from .cloud_front_vpc_origin_config import CloudFrontVpcOriginConfig


class CloudFrontOrigin(BaseModel):
    Id: StrictStr | None = None
    DomainName: StrictStr | None = None
    OriginPath: StrictStr | None = None
    CustomHeaders: CloudFrontCustomHeaders | None = None
    S3OriginConfig: CloudFrontS3OriginConfig | None = None
    CustomOriginConfig: CloudFrontCustomOriginConfig | None = None
    VpcOriginConfig: CloudFrontVpcOriginConfig | None = None
    ConnectionAttempts: StrictInt | None = None
    ConnectionTimeout: StrictInt | None = None
    ResponseCompletionTimeout: StrictInt | None = None
    OriginShield: CloudFrontOriginShield | None = None
    OriginAccessControlId: StrictStr | None = None
