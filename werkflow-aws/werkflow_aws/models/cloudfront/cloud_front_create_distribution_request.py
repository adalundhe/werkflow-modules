from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_distribution_config import CloudFrontDistributionConfig


class CloudFrontCreateDistributionRequest(BaseModel):
    DistributionConfig: CloudFrontDistributionConfig
