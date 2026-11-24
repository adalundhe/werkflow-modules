from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_traffic_policy import Route53TrafficPolicy


class Route53CreateTrafficPolicyVersionResponse(BaseModel):
    TrafficPolicy: Route53TrafficPolicy | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
