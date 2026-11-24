from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_interconnect import DirectConnectInterconnect


class DirectConnectDescribeInterconnectsResponse(BaseModel):
    interconnects: list[DirectConnectInterconnect] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
