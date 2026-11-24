from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_cloud_front_distribution_origin_item import SecurityHubAwsCloudFrontDistributionOriginItem


class SecurityHubAwsCloudFrontDistributionOrigins(BaseModel):
    Items: list[SecurityHubAwsCloudFrontDistributionOriginItem] | None = None
