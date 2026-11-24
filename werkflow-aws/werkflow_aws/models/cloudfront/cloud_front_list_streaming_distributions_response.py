from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_streaming_distribution_list import CloudFrontStreamingDistributionList


class CloudFrontListStreamingDistributionsResponse(BaseModel):
    StreamingDistributionList: CloudFrontStreamingDistributionList | None = None
    ResponseMetadata: dict[str, Any] | None = None
