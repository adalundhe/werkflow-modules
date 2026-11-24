from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_traffic_policy import Route53TrafficPolicy


class Route53UpdateTrafficPolicyCommentResponse(BaseModel):
    TrafficPolicy: Route53TrafficPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
