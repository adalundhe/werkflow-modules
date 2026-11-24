from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_private_virtual_interface_allocation import DirectConnectNewPrivateVirtualInterfaceAllocation


class DirectConnectAllocatePrivateVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    ownerAccount: StrictStr
    newPrivateVirtualInterfaceAllocation: DirectConnectNewPrivateVirtualInterfaceAllocation
