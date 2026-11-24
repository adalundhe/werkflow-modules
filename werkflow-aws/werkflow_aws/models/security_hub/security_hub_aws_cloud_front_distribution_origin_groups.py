from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_cloud_front_distribution_origin_group import SecurityHubAwsCloudFrontDistributionOriginGroup


class SecurityHubAwsCloudFrontDistributionOriginGroups(BaseModel):
    Items: list[SecurityHubAwsCloudFrontDistributionOriginGroup] | None = None
