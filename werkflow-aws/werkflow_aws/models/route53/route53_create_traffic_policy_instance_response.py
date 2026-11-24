from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_traffic_policy_instance import Route53TrafficPolicyInstance


class Route53CreateTrafficPolicyInstanceResponse(BaseModel):
    TrafficPolicyInstance: Route53TrafficPolicyInstance | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
