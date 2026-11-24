from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_cloud_front_distribution_cache_behavior import SecurityHubAwsCloudFrontDistributionCacheBehavior


class SecurityHubAwsCloudFrontDistributionCacheBehaviors(BaseModel):
    Items: list[SecurityHubAwsCloudFrontDistributionCacheBehavior] | None = None
