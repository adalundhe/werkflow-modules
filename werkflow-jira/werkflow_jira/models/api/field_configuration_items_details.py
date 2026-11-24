from __future__ import annotations
from pydantic import BaseModel
from .field_configuration_item import FieldConfigurationItem


class FieldConfigurationItemsDetails(BaseModel):
    fieldConfigurationItems: list[FieldConfigurationItem] | None = None
