from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_streaming_distribution import CloudFrontStreamingDistribution


class CloudFrontCreateStreamingDistributionResponse(BaseModel):
    StreamingDistribution: CloudFrontStreamingDistribution | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
