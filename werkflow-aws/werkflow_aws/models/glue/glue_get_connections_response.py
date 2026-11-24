from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_connection import GlueConnection


class GlueGetConnectionsResponse(BaseModel):
    ConnectionList: list[GlueConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
