from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .custom_field_context_default_value import CustomFieldContextDefaultValue


class CustomFieldContextDefaultValueUpdate(BaseModel):
    defaultValues: list[CustomFieldContextDefaultValue] | None = None
