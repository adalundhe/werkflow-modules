from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_virtual_interface import DirectConnectVirtualInterface


class DirectConnectDescribeVirtualInterfacesResponse(BaseModel):
    virtualInterfaces: list[DirectConnectVirtualInterface] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
