from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_view import ConnectView


class ConnectUpdateViewContentResponse(BaseModel):
    View: ConnectView | None = None
    ResponseMetadata: dict[str, Any] | None = None
