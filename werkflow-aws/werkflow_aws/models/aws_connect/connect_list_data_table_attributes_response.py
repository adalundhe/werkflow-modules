from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_data_table_attribute import ConnectDataTableAttribute


class ConnectListDataTableAttributesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Attributes: list[ConnectDataTableAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
