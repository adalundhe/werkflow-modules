from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_inbound_connector import QuickSightInboundConnector


class QuickSightDescribeInboundConnectorResponse(BaseModel):
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    InboundConnector: QuickSightInboundConnector | None = None
    ResponseMetadata: dict[str, Any] | None = None
