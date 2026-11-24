from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_inbound_connection import OpenSearchInboundConnection


class OpenSearchDescribeInboundConnectionsResponse(BaseModel):
    Connections: list[OpenSearchInboundConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
