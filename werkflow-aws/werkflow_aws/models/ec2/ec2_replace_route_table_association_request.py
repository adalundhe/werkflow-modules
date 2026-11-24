from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReplaceRouteTableAssociationRequest(BaseModel):
    AssociationId: StrictStr
    RouteTableId: StrictStr
    DryRun: StrictBool | None = None
