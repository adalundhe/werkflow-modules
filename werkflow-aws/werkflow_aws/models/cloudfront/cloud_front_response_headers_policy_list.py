from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_response_headers_policy_summary import CloudFrontResponseHeadersPolicySummary


class CloudFrontResponseHeadersPolicyList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontResponseHeadersPolicySummary] | None = None
