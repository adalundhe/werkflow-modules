from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Route53ARCControlPanel(BaseModel):
    ClusterArn: StrictStr | None = None
    ControlPanelArn: StrictStr | None = None
    DefaultControlPanel: StrictBool | None = None
    Name: StrictStr | None = None
    RoutingControlCount: StrictInt | None = None
    Status: StrictStr | None = None
    Owner: StrictStr | None = None
