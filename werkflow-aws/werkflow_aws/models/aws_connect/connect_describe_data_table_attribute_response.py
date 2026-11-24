from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_data_table_attribute import ConnectDataTableAttribute


class ConnectDescribeDataTableAttributeResponse(BaseModel):
    Attribute: ConnectDataTableAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
