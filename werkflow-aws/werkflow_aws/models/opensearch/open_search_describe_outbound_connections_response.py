from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_outbound_connection import OpenSearchOutboundConnection


class OpenSearchDescribeOutboundConnectionsResponse(BaseModel):
    Connections: list[OpenSearchOutboundConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
