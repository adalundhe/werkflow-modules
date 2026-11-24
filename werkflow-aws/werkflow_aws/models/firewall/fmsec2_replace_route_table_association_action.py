from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_action_target import FMSActionTarget


class FMSEC2ReplaceRouteTableAssociationAction(BaseModel):
    Description: StrictStr | None = None
    AssociationId: FMSActionTarget | None = None
    RouteTableId: FMSActionTarget | None = None
