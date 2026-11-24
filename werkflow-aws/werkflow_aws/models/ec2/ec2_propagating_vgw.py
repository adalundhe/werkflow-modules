from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PropagatingVgw(BaseModel):
    GatewayId: StrictStr | None = None
