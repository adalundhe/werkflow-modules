from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_listener_attribute import ELBv2ListenerAttribute


class ELBv2DescribeListenerAttributesResponse(BaseModel):
    Attributes: list[ELBv2ListenerAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
