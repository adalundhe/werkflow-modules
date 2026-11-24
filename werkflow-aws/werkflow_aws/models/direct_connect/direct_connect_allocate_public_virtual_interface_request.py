from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_public_virtual_interface_allocation import DirectConnectNewPublicVirtualInterfaceAllocation


class DirectConnectAllocatePublicVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    ownerAccount: StrictStr
    newPublicVirtualInterfaceAllocation: DirectConnectNewPublicVirtualInterfaceAllocation
