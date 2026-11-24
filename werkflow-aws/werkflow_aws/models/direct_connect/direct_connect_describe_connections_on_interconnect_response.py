from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_connection import DirectConnectConnection


class DirectConnectDescribeConnectionsOnInterconnectResponse(BaseModel):
    connections: list[DirectConnectConnection] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
