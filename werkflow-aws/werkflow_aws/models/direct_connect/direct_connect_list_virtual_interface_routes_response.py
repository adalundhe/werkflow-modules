from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_route import DirectConnectRoute


class DirectConnectListVirtualInterfaceRoutesResponse(BaseModel):
    virtualInterfaceId: StrictStr | None = None
    routes: list[DirectConnectRoute] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
