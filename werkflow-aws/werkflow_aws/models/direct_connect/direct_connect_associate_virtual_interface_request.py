from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociateVirtualInterfaceRequest(BaseModel):
    virtualInterfaceId: StrictStr
    connectionId: StrictStr
