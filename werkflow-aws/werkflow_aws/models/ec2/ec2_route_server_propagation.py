from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteServerPropagation(BaseModel):
    RouteServerId: StrictStr | None = None
    RouteTableId: StrictStr | None = None
    State: StrictStr | None = None
