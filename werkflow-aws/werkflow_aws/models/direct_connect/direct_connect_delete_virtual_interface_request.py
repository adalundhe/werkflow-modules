from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteVirtualInterfaceRequest(BaseModel):
    virtualInterfaceId: StrictStr
