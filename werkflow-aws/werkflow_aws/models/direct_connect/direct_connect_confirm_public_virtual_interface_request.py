from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmPublicVirtualInterfaceRequest(BaseModel):
    virtualInterfaceId: StrictStr
