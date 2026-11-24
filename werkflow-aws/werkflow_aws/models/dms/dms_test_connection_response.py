from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_connection import DMSConnection


class DMSTestConnectionResponse(BaseModel):
    Connection: DMSConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
