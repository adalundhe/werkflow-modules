from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_distribution import CloudFrontDistribution


class CloudFrontCreateDistributionResponse(BaseModel):
    Distribution: CloudFrontDistribution | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
