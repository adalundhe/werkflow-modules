from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_listener import ELBv2Listener


class ELBv2DescribeListenersResponse(BaseModel):
    Listeners: list[ELBv2Listener] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
