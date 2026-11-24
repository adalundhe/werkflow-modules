from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_traffic_policy_instance import Route53TrafficPolicyInstance


class Route53ListTrafficPolicyInstancesByPolicyResponse(BaseModel):
    TrafficPolicyInstances: list[Route53TrafficPolicyInstance] | None = None
    HostedZoneIdMarker: StrictStr | None = None
    TrafficPolicyInstanceNameMarker: StrictStr | None = None
    TrafficPolicyInstanceTypeMarker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
