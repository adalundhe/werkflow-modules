from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCUpdateControlPanelRequest(BaseModel):
    ControlPanelArn: StrictStr
    ControlPanelName: StrictStr
