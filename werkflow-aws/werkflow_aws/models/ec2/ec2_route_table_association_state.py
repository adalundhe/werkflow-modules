from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteTableAssociationState(BaseModel):
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
