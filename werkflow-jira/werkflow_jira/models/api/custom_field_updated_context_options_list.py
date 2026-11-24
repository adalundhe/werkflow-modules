from __future__ import annotations
from pydantic import BaseModel
from .custom_field_option_update import CustomFieldOptionUpdate


class CustomFieldUpdatedContextOptionsList(BaseModel):
    options: list[CustomFieldOptionUpdate] | None = None
