from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_view import ConnectView


class ConnectDescribeViewResponse(BaseModel):
    View: ConnectView | None = None
    ResponseMetadata: dict[str, Any] | None = None
