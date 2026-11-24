from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_arc_routing_control import Route53ARCRoutingControl


class Route53ARCListRoutingControlsResponse(BaseModel):
    NextToken: StrictStr | None = None
    RoutingControls: list[Route53ARCRoutingControl] | None = None
    ResponseMetadata: dict[str, Any] | None = None
