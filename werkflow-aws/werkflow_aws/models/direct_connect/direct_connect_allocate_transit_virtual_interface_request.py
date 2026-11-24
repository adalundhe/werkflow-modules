from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_transit_virtual_interface_allocation import DirectConnectNewTransitVirtualInterfaceAllocation


class DirectConnectAllocateTransitVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    ownerAccount: StrictStr
    newTransitVirtualInterfaceAllocation: DirectConnectNewTransitVirtualInterfaceAllocation
