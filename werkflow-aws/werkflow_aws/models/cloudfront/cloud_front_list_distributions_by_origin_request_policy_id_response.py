from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_distribution_id_list import CloudFrontDistributionIdList


class CloudFrontListDistributionsByOriginRequestPolicyIdResponse(BaseModel):
    DistributionIdList: CloudFrontDistributionIdList | None = None
    ResponseMetadata: dict[str, Any] | None = None
