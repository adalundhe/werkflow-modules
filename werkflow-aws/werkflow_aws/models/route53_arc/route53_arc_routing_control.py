from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCRoutingControl(BaseModel):
    ControlPanelArn: StrictStr | None = None
    Name: StrictStr | None = None
    RoutingControlArn: StrictStr | None = None
    Status: StrictStr | None = None
    Owner: StrictStr | None = None
