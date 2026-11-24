from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_action_target import FMSActionTarget


class FMSEC2AssociateRouteTableAction(BaseModel):
    Description: StrictStr | None = None
    RouteTableId: FMSActionTarget | None = None
    SubnetId: FMSActionTarget | None = None
    GatewayId: FMSActionTarget | None = None
