from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53ARCListRoutingControlsRequest(BaseModel):
    ControlPanelArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
