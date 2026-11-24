from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_distribution_list import CloudFrontDistributionList


class CloudFrontListDistributionsByAnycastIpListIdResponse(BaseModel):
    DistributionList: CloudFrontDistributionList | None = None
    ResponseMetadata: dict[str, Any] | None = None
