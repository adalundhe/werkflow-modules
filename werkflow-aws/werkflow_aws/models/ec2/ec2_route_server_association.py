from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteServerAssociation(BaseModel):
    RouteServerId: StrictStr | None = None
    VpcId: StrictStr | None = None
    State: StrictStr | None = None
