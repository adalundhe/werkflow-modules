from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_public_virtual_interface import DirectConnectNewPublicVirtualInterface


class DirectConnectCreatePublicVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    newPublicVirtualInterface: DirectConnectNewPublicVirtualInterface
