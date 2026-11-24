from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_origin_request_policy_summary import CloudFrontOriginRequestPolicySummary


class CloudFrontOriginRequestPolicyList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOriginRequestPolicySummary] | None = None
