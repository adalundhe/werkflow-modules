from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmTransitVirtualInterfaceRequest(BaseModel):
    virtualInterfaceId: StrictStr
    directConnectGatewayId: StrictStr
