from __future__ import annotations
from pydantic import BaseModel
from .connect_custom_field_value import ConnectCustomFieldValue


class ConnectCustomFieldValues(BaseModel):
    updateValueList: list[ConnectCustomFieldValue] | None = None
