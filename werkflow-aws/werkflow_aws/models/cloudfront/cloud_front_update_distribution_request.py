from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_distribution_config import CloudFrontDistributionConfig


class CloudFrontUpdateDistributionRequest(BaseModel):
    DistributionConfig: CloudFrontDistributionConfig
    Id: StrictStr
    IfMatch: StrictStr | None = None
