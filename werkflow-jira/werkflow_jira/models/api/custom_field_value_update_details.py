from __future__ import annotations
from pydantic import BaseModel
from .custom_field_value_update import CustomFieldValueUpdate


class CustomFieldValueUpdateDetails(BaseModel):
    updates: list[CustomFieldValueUpdate] | None = None
