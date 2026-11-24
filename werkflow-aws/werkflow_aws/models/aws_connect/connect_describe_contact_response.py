from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_contact import ConnectContact


class ConnectDescribeContactResponse(BaseModel):
    Contact: ConnectContact | None = None
    ResponseMetadata: dict[str, Any] | None = None
