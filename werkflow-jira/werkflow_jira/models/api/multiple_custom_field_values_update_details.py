from __future__ import annotations
from pydantic import BaseModel
from .multiple_custom_field_values_update import MultipleCustomFieldValuesUpdate


class MultipleCustomFieldValuesUpdateDetails(BaseModel):
    updates: list[MultipleCustomFieldValuesUpdate] | None = None
