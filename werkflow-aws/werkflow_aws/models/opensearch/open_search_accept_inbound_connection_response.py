from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_inbound_connection import OpenSearchInboundConnection


class OpenSearchAcceptInboundConnectionResponse(BaseModel):
    Connection: OpenSearchInboundConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
