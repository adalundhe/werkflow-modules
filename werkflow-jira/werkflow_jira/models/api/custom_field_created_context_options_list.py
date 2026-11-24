from __future__ import annotations
from pydantic import BaseModel
from .custom_field_context_option import CustomFieldContextOption


class CustomFieldCreatedContextOptionsList(BaseModel):
    options: list[CustomFieldContextOption] | None = None
