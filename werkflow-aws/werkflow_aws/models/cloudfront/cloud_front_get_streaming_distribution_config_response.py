from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_streaming_distribution_config import CloudFrontStreamingDistributionConfig


class CloudFrontGetStreamingDistributionConfigResponse(BaseModel):
    StreamingDistributionConfig: CloudFrontStreamingDistributionConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
