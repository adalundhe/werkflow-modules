from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCCreateRoutingControlRequest(BaseModel):
    ClusterArn: StrictStr
    RoutingControlName: StrictStr
    ClientToken: StrictStr | None = None
    ControlPanelArn: StrictStr | None = None
