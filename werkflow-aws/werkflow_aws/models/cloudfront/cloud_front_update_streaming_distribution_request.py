from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_streaming_distribution_config import CloudFrontStreamingDistributionConfig


class CloudFrontUpdateStreamingDistributionRequest(BaseModel):
    StreamingDistributionConfig: CloudFrontStreamingDistributionConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
