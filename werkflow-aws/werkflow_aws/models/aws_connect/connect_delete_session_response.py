from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ConnectDeleteSessionResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
