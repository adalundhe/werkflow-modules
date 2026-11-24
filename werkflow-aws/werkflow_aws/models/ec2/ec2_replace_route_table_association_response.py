from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_route_table_association_state import EC2RouteTableAssociationState


class EC2ReplaceRouteTableAssociationResponse(BaseModel):
    NewAssociationId: StrictStr | None = None
    AssociationState: EC2RouteTableAssociationState | None = None
    ResponseMetadata: dict[str, Any] | None = None
