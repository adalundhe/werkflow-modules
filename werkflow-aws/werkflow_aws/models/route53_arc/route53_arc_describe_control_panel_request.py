from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCDescribeControlPanelRequest(BaseModel):
    ControlPanelArn: StrictStr
