from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_distribution_config import CloudFrontDistributionConfig
from .cloud_front_tags import CloudFrontTags


class CloudFrontDistributionConfigWithTags(BaseModel):
    DistributionConfig: CloudFrontDistributionConfig
    Tags: CloudFrontTags
