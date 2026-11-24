from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_traffic_policy_summary import Route53TrafficPolicySummary


class Route53ListTrafficPoliciesResponse(BaseModel):
    TrafficPolicySummaries: list[Route53TrafficPolicySummary] | None = None
    IsTruncated: StrictBool | None = None
    TrafficPolicyIdMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
