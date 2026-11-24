from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_connection import GlueConnection


class GlueGetConnectionResponse(BaseModel):
    Connection: GlueConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
