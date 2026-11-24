from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_arc_control_panel import Route53ARCControlPanel


class Route53ARCListControlPanelsResponse(BaseModel):
    ControlPanels: list[Route53ARCControlPanel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
