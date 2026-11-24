from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_action_target import FMSActionTarget


class FMSEC2CopyRouteTableAction(BaseModel):
    Description: StrictStr | None = None
    VpcId: FMSActionTarget | None = None
    RouteTableId: FMSActionTarget | None = None
