from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_new_transit_virtual_interface import DirectConnectNewTransitVirtualInterface


class DirectConnectCreateTransitVirtualInterfaceRequest(BaseModel):
    connectionId: StrictStr
    newTransitVirtualInterface: DirectConnectNewTransitVirtualInterface
