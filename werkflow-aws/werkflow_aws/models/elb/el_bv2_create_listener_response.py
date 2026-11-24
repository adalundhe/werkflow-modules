from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_listener import ELBv2Listener


class ELBv2CreateListenerResponse(BaseModel):
    Listeners: list[ELBv2Listener] | None = None
    ResponseMetadata: dict[str, Any] | None = None
