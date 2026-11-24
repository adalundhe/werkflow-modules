from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_attribute import ConnectAttribute


class ConnectListInstanceAttributesResponse(BaseModel):
    Attributes: list[ConnectAttribute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
