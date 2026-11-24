from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_cache_policy_summary import CloudFrontCachePolicySummary


class CloudFrontCachePolicyList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontCachePolicySummary] | None = None
