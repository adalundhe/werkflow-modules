from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_arc_routing_control import Route53ARCRoutingControl


class Route53ARCDescribeRoutingControlResponse(BaseModel):
    RoutingControl: Route53ARCRoutingControl | None = None
    ResponseMetadata: dict[str, Any] | None = None
