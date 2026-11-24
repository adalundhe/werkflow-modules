from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmPrivateVirtualInterfaceRequest(BaseModel):
    virtualInterfaceId: StrictStr
    virtualGatewayId: StrictStr | None = None
    directConnectGatewayId: StrictStr | None = None
