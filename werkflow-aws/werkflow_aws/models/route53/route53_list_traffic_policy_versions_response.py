from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_traffic_policy import Route53TrafficPolicy


class Route53ListTrafficPolicyVersionsResponse(BaseModel):
    TrafficPolicies: list[Route53TrafficPolicy] | None = None
    IsTruncated: StrictBool | None = None
    TrafficPolicyVersionMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
