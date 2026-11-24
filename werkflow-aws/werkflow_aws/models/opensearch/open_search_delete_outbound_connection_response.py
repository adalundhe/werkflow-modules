from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_outbound_connection import OpenSearchOutboundConnection


class OpenSearchDeleteOutboundConnectionResponse(BaseModel):
    Connection: OpenSearchOutboundConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
