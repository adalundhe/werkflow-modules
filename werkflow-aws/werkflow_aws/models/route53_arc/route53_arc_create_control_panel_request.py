from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCCreateControlPanelRequest(BaseModel):
    ClusterArn: StrictStr
    ControlPanelName: StrictStr
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
