from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectVirtualGateway(BaseModel):
    virtualGatewayId: StrictStr | None = None
    virtualGatewayState: StrictStr | None = None
