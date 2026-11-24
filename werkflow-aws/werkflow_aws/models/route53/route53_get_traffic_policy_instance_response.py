from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_traffic_policy_instance import Route53TrafficPolicyInstance


class Route53GetTrafficPolicyInstanceResponse(BaseModel):
    TrafficPolicyInstance: Route53TrafficPolicyInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
