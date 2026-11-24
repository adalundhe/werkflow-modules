from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_distribution_config import CloudFrontDistributionConfig


class CloudFrontGetDistributionConfigResponse(BaseModel):
    DistributionConfig: CloudFrontDistributionConfig | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
