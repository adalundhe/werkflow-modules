from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_connection import DMSConnection


class DMSDescribeConnectionsResponse(BaseModel):
    Marker: StrictStr | None = None
    Connections: list[DMSConnection] | None = None
    ResponseMetadata: dict[str, Any] | None = None
