from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_vpc_connection import QuickSightVPCConnection


class QuickSightDescribeVPCConnectionResponse(BaseModel):
    VPCConnection: QuickSightVPCConnection | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
