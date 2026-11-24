from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_vpc_connection_summary import QuickSightVPCConnectionSummary


class QuickSightListVPCConnectionsResponse(BaseModel):
    VPCConnectionSummaries: list[QuickSightVPCConnectionSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
