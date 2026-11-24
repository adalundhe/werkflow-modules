from __future__ import annotations
from pydantic import BaseModel
from .connect_field_value import ConnectFieldValue


class ConnectUpdateCaseActionDefinition(BaseModel):
    Fields: list[ConnectFieldValue] | None = None
