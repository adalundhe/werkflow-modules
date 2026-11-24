from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_cloud_front_distribution_origin_custom_origin_config import SecurityHubAwsCloudFrontDistributionOriginCustomOriginConfig
from .security_hub_aws_cloud_front_distribution_origin_s3_origin_config import SecurityHubAwsCloudFrontDistributionOriginS3OriginConfig


class SecurityHubAwsCloudFrontDistributionOriginItem(BaseModel):
    DomainName: StrictStr | None = None
    Id: StrictStr | None = None
    OriginPath: StrictStr | None = None
    S3OriginConfig: SecurityHubAwsCloudFrontDistributionOriginS3OriginConfig | None = None
    CustomOriginConfig: SecurityHubAwsCloudFrontDistributionOriginCustomOriginConfig | None = None
