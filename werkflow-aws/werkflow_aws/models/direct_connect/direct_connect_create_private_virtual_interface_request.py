from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_private_virtual_interface import DirectConnectNewPrivateVirtualInterface


class DirectConnectCreatePrivateVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    newPrivateVirtualInterface: DirectConnectNewPrivateVirtualInterface
