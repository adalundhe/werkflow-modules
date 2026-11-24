from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_streaming_distribution_config import CloudFrontStreamingDistributionConfig
from .cloud_front_tags import CloudFrontTags


class CloudFrontStreamingDistributionConfigWithTags(BaseModel):
    StreamingDistributionConfig: CloudFrontStreamingDistributionConfig
    Tags: CloudFrontTags
