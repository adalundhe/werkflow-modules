from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_quick_connect import ConnectQuickConnect


class ConnectDescribeQuickConnectResponse(BaseModel):
    QuickConnect: ConnectQuickConnect | None = None
    ResponseMetadata: dict[str, Any] | None = None
