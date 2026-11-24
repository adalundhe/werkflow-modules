from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_arc_control_panel import Route53ARCControlPanel


class Route53ARCDescribeControlPanelResponse(BaseModel):
    ControlPanel: Route53ARCControlPanel | None = None
    ResponseMetadata: dict[str, Any] | None = None
