from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_queue import ConnectQueue


class ConnectDescribeQueueResponse(BaseModel):
    Queue: ConnectQueue | None = None
    ResponseMetadata: dict[str, Any] | None = None
