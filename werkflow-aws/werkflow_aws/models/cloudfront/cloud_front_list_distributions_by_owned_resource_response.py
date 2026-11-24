from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_distribution_id_owner_list import CloudFrontDistributionIdOwnerList


class CloudFrontListDistributionsByOwnedResourceResponse(BaseModel):
    DistributionList: CloudFrontDistributionIdOwnerList | None = None
    ResponseMetadata: dict[str, Any] | None = None
