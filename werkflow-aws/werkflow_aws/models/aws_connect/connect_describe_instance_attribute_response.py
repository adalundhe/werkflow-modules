from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_attribute import ConnectAttribute


class ConnectDescribeInstanceAttributeResponse(BaseModel):
    Attribute: ConnectAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
