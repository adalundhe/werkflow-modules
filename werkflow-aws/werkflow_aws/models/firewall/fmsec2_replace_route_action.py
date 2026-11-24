from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_action_target import FMSActionTarget


class FMSEC2ReplaceRouteAction(BaseModel):
    Description: StrictStr | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationPrefixListId: StrictStr | None = None
    DestinationIpv6CidrBlock: StrictStr | None = None
    GatewayId: FMSActionTarget | None = None
    RouteTableId: FMSActionTarget | None = None
